package com.example.crawlingtest;

import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class WordGenerator {

    private String word;
    private List<String> alphabets = new ArrayList<>();
    public Set<String> allCombinations = new HashSet<>();

    public void setWord(String word) {
        this.word = word;
        getAlphabets();
    }

    public void getAlphabets(){
        Set<String> temp = new HashSet<>();
        temp.addAll(Arrays.stream(word.split("")).toList());
        alphabets.addAll(temp);
    }

    public void generateCombinations() {
        allCombinations.clear();
        for (int i = 3; i < alphabets.size(); i++) {
            generateCombination(0,i,new ArrayList<>());
        }
    }
    private void generateCombination(int index, int size, List<String> alphabetList) {
        if (alphabetList.size() == size) {
            makeWord(alphabetList);
            return;
        }
        for (int i = index; i < alphabets.size(); i++) {
            alphabetList.add(alphabets.get(i));
            generateCombination(i+1, size, alphabetList);
            alphabetList.remove(alphabetList.size()-1);
        }
    }
    private void makeWord(List<String> alphabetList){
        StringBuilder sb = new StringBuilder();
        for(String s: alphabetList){
            sb.append(s);
        }
        allCombinations.add(sb.toString());
    }
}
