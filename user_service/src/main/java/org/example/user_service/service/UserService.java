package org.example.user_service.service;

import org.springframework.stereotype.Service;

@Service
public class UserService {

    public void serviceTest1(){
        System.out.println("in Service Test 1");
        serviceTest2();
        serviceTest3();
    }

    public void serviceTest2(){
        System.out.println("in Service Test 2");
    }

    public void serviceTest3(){
        System.out.println("in Service Test 3");
    }

}
