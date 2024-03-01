package com.example.crawlingtest;

import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

@Service
public class Papago {
    private static final String API_URL = "https://openapi.naver.com/v1/papago/n2mt";
    private static final String CLIENT_ID = "XjKfRs1qLmbvq1zVQUhe";
    private static final String CLIENT_SECRET = "8fGTL2W4qb";

    private static WebClient webClient = null;

    public Papago(){
        this.webClient = WebClient.builder()
                .baseUrl(API_URL)
                .defaultHeader("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
                .defaultHeader("X-Naver-Client-Id", CLIENT_ID)
                .defaultHeader("X-Naver-Client-Secret", CLIENT_SECRET)
                .build();
    }

    public static void translate(String sourceLang, String targetLang, String text) {
        String requestBody = "source=" + sourceLang + "&target=" + targetLang + "&text=" + text;


        System.out.println("requestBody = " + requestBody);
        webClient.post()
                .bodyValue(requestBody)
                .retrieve()
                .onStatus(status -> status.isError(), response -> {
                    System.out.println("An error occurred: " + response.statusCode());
                    return Mono.empty();
                })
                .bodyToMono(TranslationResponse.class)
                .subscribe(response -> {
                    String translatedText = response.getMessage().getResult().getTranslatedText();
                    System.out.println(translatedText);
                }, error -> {
                    System.out.println("Error handling: " + error.getMessage());
                });
    }

    public static void main(String[] args) {
        Papago papago = new Papago();
        papago.translate("en","ko","ers");
    }
}
