FROM openjdk:17-jdk

# 작업 디렉토리 설정
WORKDIR /app

# 포트 지정
EXPOSE 8080

# OpenTelemetry Agent 파일을 이미지에 복사
ADD https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/download/v2.3.0/opentelemetry-javaagent.jar /opentelemetry-javaagent.jar

# 애플리케이션의 jar 파일을 이미지에 복사
COPY build/libs/telemetry_test2-0.0.1-SNAPSHOT.jar /app/telemetry_test2.jar

# OpenTelemetry Java Agent 실행 옵션 설정
#ENV JAVA_TOOL_OPTIONS="-javaagent:/opentelemetry-javaagent.jar"
ENV OTEL_EXPORTER_OTLP_ENDPOINT="http://collector:4318/v1/traces"
ENV OTEL_EXPORTER_OTLP_ENDPOINT_LOGS="http://collector:4318/v1/logs"
ENV OTEL_EXPORTER_OTLP_ENDPOINT_METRICS="http://collector:4318/v1/metrics"
#ENV OTEL_RESOURCE_ATTRIBUTES="service.name=telemetry_test2"

# 애플리케이션 실행
CMD ["java", "-javaagent:/opentelemetry-javaagent.jar", "-Dotel.service.name=telemetry_test2", "-Dotel.exporter.otlp.protocol=http/protobuf", "-Dotel.exporter.otlp.endpoint=http://collector:4318/", "-jar", "/app/telemetry_test2.jar"]
#CMD ["java", "-javaagent:/opentelemetry-javaagent.jar", "-Dotel.service.name=telemetry_test2", "-Dotel.exporter.otlp.protocol=http/protobuf", "-jar", "/app/telemetry_test2.jar"]
