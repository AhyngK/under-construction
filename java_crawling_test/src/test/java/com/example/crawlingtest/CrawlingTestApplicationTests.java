package com.example.crawlingtest;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class CrawlingTestApplicationTests {
	@Autowired
	private CrawlingMain crawlingMain;

	@Autowired
	private WordGenerator wordGenerator;

	@Autowired
	private Papago papago;

	@Test
	void contextLoads() {
		crawlingMain.getData();
	}

	@Test
	void makeWord(){
		String word = "combination";
		wordGenerator.setWord(word);
		wordGenerator.generateCombinations();
		System.out.println("test: "+wordGenerator.allCombinations.toString());
	}

	@Test
	void testPapago(){
		papago.translate("en","ko","text");
	}

}
