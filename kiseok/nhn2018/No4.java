package nhn2018;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class No4 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        
        int [] powerPole = new int [n];
        for (int i=0; i<n; i++) {
            powerPole[i] = Integer.parseInt(br.readLine().trim());
        }
        Arrays.sort(powerPole);

        // 전봇대간 거리 구하기
        int [] distance = new int [n-1];
        for (int i=0; i<n-1; i++) {
            distance[i] = Math.abs(powerPole[i] - powerPole[i+1]);
        }
        
        // 전봇대간 거리의 최대 공약수 구하기
        int gcd = distance[0];
        for (int i=1; i<n-1; i++) {
            if (gcd > distance[i]) {
                gcd = GCD(gcd, distance[i]);
            } else {
                gcd = GCD(distance[i], gcd);
            }
        }
        
        // 전봇대간 거리를 최대 공약수로 나누면 최소 필요한 전봇대 수를 구할 수 있다.
        int result = 0;
        for (int i=0; i<n-1; i++) {
            result += (distance[i]/gcd)-1;
        }
        
        System.out.println(result);
    }
    
    private static int GCD(int a, int b) {
        if (b == 0){
            return a;
        }
        return GCD(b, a % b);
    }
}
