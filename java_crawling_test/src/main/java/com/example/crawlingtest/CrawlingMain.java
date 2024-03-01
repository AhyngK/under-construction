package com.example.crawlingtest;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.springframework.stereotype.Service;

import java.io.IOException;

@Service
public class CrawlingMain {
    private String url = "https://edition.cnn.com/";

    public void getData(){
        try {
            Document document = Jsoup.connect(url).get();
            System.out.println("title: "+document.title());

            Elements headlines = document.select("h2.container__title_url-text.container_lead-package__title_url-text");
            for(Element headLine: headlines){
                System.out.println("headline: "+ headLine.text());
            }

        } catch (IOException e){
            e.printStackTrace();
        }
    }

}
