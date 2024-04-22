package org.example.kafka_consumer_test;

import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

@Component
public class KafkaMessgaeListener {
    @KafkaListener(topics = "otel-traces", groupId = "otel")
    public void listen(String message) {
        System.out.println("Received message: " + message);
    }
}
