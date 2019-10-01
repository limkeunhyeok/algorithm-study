package nhn2018;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No3 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        
        int [] toyWeight = new int [n];
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            toyWeight[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(toyWeight);
        
        int result = 1;
        // 기준 무게
        int referenceWeight = toyWeight[0];
        for (int i=0; i<n; i++) {
            if (referenceWeight+4 < toyWeight[i]) {
                referenceWeight = toyWeight[i];
                result++;
            }
        }
        
        System.out.println(result);
    }
}
