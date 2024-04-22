package org.example.telemetry_test2.service;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class TestService {
    public void testMethod1(){
        System.out.println("In TestMethod1");
    }

    public void testMethod2(){
        System.out.println("In TestMethod2");
        testMethod3();
    }

    private void testMethod3(){
        System.out.println("In TestMethod3");
    }

}
