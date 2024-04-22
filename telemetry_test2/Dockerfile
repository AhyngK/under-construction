FROM openjdk:17

# OpenTelemetry Agent 파일을 이미지에 복사
ADD https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/download/v2.3.0/opentelemetry-javaagent.jar /opt/opentelemetry-javaagent.jar

# 애플리케이션의 jar 파일을 이미지에 복사
COPY build/libs/telemetry_test2-0.0.1-SNAPSHOT.jar /app/telemetry_test2-0.0.1-SNAPSHOT.jar

# OpenTelemetry Java Agent 실행 옵션 설정
ENV JAVA_TOOL_OPTIONS="-javaagent:/opt/opentelemetry-javaagent.jar"

# OpenTelemetry OTLP Exporter와 관련된 환경 변수 설정
ENV OTEL_EXPORTER_OTLP_ENDPOINT="http://otel-collector:4317"
ENV OTEL_RESOURCE_ATTRIBUTES="service.name=telemetry_test2"

# 애플리케이션 실행
CMD ["java", "-jar", "/app/telemetry_test2-0.0.1-SNAPSHOT.jar"]
