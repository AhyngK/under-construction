package org.example.user_service.config;

import io.opentelemetry.api.GlobalOpenTelemetry;
import io.opentelemetry.api.OpenTelemetry;
import io.opentelemetry.api.trace.SpanKind;
import io.opentelemetry.api.trace.Tracer;
import io.opentelemetry.contrib.sampler.RuleBasedRoutingSampler;
import io.opentelemetry.exporter.logging.LoggingSpanExporter;
import io.opentelemetry.exporter.otlp.http.trace.OtlpHttpSpanExporter;
import io.opentelemetry.exporter.otlp.trace.OtlpGrpcSpanExporter;
import io.opentelemetry.sdk.OpenTelemetrySdk;
import io.opentelemetry.sdk.autoconfigure.spi.AutoConfigurationCustomizerProvider;
import io.opentelemetry.sdk.trace.SdkTracerProvider;
import io.opentelemetry.sdk.trace.export.BatchSpanProcessor;
import io.opentelemetry.sdk.trace.export.SimpleSpanProcessor;
import io.opentelemetry.sdk.trace.export.SpanExporter;
import io.opentelemetry.sdk.trace.samplers.Sampler;
import io.opentelemetry.semconv.SemanticAttributes;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.Collections;
import java.util.Map;
import java.util.concurrent.TimeUnit;

@Configuration
public class OpenTelemetryConfig {

    @Bean
    public OpenTelemetry openTelemetry() {
        SdkTracerProvider sdkTracerProvider = SdkTracerProvider.builder()
            .addSpanProcessor(SimpleSpanProcessor.create(LoggingSpanExporter.create()))
            .build();

        return OpenTelemetrySdk.builder()
            .setTracerProvider(sdkTracerProvider)
            .build();
    }

//    @Bean
//    public Tracer tracer() {
//        OtlpGrpcSpanExporter spanExporter = OtlpGrpcSpanExporter.builder()
//            .setEndpoint("http://your-otel-collector:4317")
//            .setTimeout(2, TimeUnit.SECONDS)
//            .build();
//
//        SdkTracerProvider sdkTracerProvider = SdkTracerProvider.builder()
//            .addSpanProcessor(BatchSpanProcessor.builder(spanExporter).build())
//            .build();
//
//        OpenTelemetrySdk openTelemetrySdk = OpenTelemetrySdk.builder()
//            .setTracerProvider(sdkTracerProvider)
//            .buildAndRegisterGlobal();
//
//        // Return a tracer instance from your SDK
//        return openTelemetrySdk.getTracer("your-application-name");
//    }

    // OpenTelemetry의 추적 데이터를 보내는 과정에서 HTTP 헤더를 커스터마이즈
    @Bean
    // OpenTelemetry의 자동 구성 프로세스에 훅(hook)을 제공하여, 구성을 커스터마이즈
    public AutoConfigurationCustomizerProvider otelCustomizer() {
    return p ->
            // 스팬 익스포터의 동작을 커스터마이즈
        p.addSpanExporterCustomizer(
            (exporter, config) -> {
                // OtlpHttpSpanExporter는 OTLP(Observability Telemetry Protocol)를 사용하여 HTTP를 통해 데이터를 전송하는 익스포터
              if (exporter instanceof OtlpHttpSpanExporter) {
                return ((OtlpHttpSpanExporter) exporter)
                    .toBuilder().setHeaders(this::headers).build();
              }
              return exporter;
            });
    }

    private Map<String, String> headers() {
    return Collections.singletonMap("Authorization", "Bearer " + refreshToken());
    }

    private String refreshToken() {
    // e.g. read the token from a kubernetes secret
    return "token";
    }
}
