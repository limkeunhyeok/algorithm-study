package nhn2018;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No6 {
    
    private static int maximumPrice=0;
    
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        
        int [] appleSetPrice = new int [n];
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            appleSetPrice[i] = Integer.parseInt(st.nextToken());
        }
        
//        maximumPrice(appleSetPrice, 0, n);
//        System.out.println(maximumPrice);
        
        System.out.println(maximumPrice2(appleSetPrice, n));
    }
    
    
    // DP(dynamic programming)가 들어가야 함.
    private static void maximumPrice(int [] appleSetPrice, int totalPrice, int numOfApple) {
        if (numOfApple == 0) {
            if (totalPrice > maximumPrice) {
                maximumPrice = totalPrice;
            }
        } else {
            for (int i=numOfApple; i>0; i--)
                maximumPrice(appleSetPrice, totalPrice + appleSetPrice[i-1], numOfApple-i);
        }
    }
    
    // DP 적용
    private static int maximumPrice2(int [] appleSetPrice, int numOfApple) {
        for (int i=0; i<numOfApple; i++) {
            int tmpMax = appleSetPrice[i];
            for (int j=0; j<i; j++) {
                tmpMax = Math.max(tmpMax, appleSetPrice[i-j-1] + appleSetPrice[j]);
            }
            appleSetPrice[i] = tmpMax;
        }
        
        return appleSetPrice[numOfApple-1];
    }
}
