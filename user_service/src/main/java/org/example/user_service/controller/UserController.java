package org.example.user_service.controller;

import lombok.RequiredArgsConstructor;
import org.example.user_service.service.UserService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
public class UserController {
    private final UserService userService;

    @GetMapping("/")
    public ResponseEntity getTest(){
        System.out.println("In GetTest1");
        return ResponseEntity.status(HttpStatus.OK)
                .build();
    }

    @GetMapping("/method")
    public ResponseEntity getMethodTest(){
        System.out.println("In Get Method Test");
        userService.serviceTest1();
        return ResponseEntity.status(HttpStatus.OK)
                .build();
    }
}
