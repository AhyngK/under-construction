FROM openjdk:17

# 작업 디렉토리 설정
WORKDIR /app

# 애플리케이션의 jar 파일을 이미지 내부의 /app 디렉토리로 복사
COPY build/libs/kafka_consumer_test-0.0.1-SNAPSHOT.jar /app/app.jar

# 애플리케이션 실행
CMD ["java", "-jar", "/app/app.jar"]