package org.example.telemetry_test2.controller;

import lombok.RequiredArgsConstructor;
import org.example.telemetry_test2.service.TestService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
public class TestController {
    private final TestService testService;

    @GetMapping("/")
    public ResponseEntity getTest(){
        testService.testMethod1();
        return ResponseEntity.ok().build();
    }

    @GetMapping("/method")
    public ResponseEntity methodTest(){
        testService.testMethod2();
        return ResponseEntity.ok().build();
    }
}
