package nhn2018;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No2 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testCase = Integer.parseInt(br.readLine().trim());
        
        while(testCase-->0) {
            String word = br.readLine().trim();
            int lengthOfWord = word.length();
            int halfLengthOfWord = word.length()/2;
            
            int result = 0;
            
            for (int i=0; i<halfLengthOfWord; i++) {
                char front = word.charAt(i);
                char back = word.charAt(lengthOfWord-1-i);
                
                result += Math.abs(back - front);
            }
            System.out.println(result);
        }
    }
}
