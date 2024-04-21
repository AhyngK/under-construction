package org.example.user_service.aop;

import io.opentelemetry.api.OpenTelemetry;
import io.opentelemetry.api.trace.Span;
import io.opentelemetry.api.trace.Tracer;
import io.opentelemetry.context.Scope;
import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.AfterReturning;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.annotation.Lazy;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class LoggingAspect {
    private static final Logger logger = LoggerFactory.getLogger(LoggingAspect.class);
    private final Tracer tracer;

    public LoggingAspect(@Lazy OpenTelemetry openTelemetry) {
        this.tracer = openTelemetry.getTracer("exampleTracer");
    }

    @Before("execution(* org.example.user_service.*.*.*(..))")
     public void beforeMethod(JoinPoint joinPoint) {
        String methodName = joinPoint.getSignature().getName();
        Span span = tracer.spanBuilder(methodName).startSpan();
        try (Scope scope = span.makeCurrent()) {
            // Log something or add attributes to span if necessary
        } finally {
            span.end();
        }
    }

    @AfterReturning(pointcut = "execution(* org.example.user_service.*.*.*(..))", returning = "result")
    public void logMethodReturn(JoinPoint joinPoint, Object result) {
        String methodName = joinPoint.getSignature().getName();
        logger.info("After method: " + methodName + ", returning: " + result);
    }
}
