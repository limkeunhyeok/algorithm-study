package algo;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class FANMEETING {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int testCase = Integer.parseInt(br.readLine().trim());
        while (testCase-->0) {
            String hyperSeniorString = br.readLine();
            String fansString = br.readLine();
            
            int hyperSeniorCount = hyperSeniorString.length();
            int fanCount = fansString.length();
            
            if (hyperSeniorCount > fanCount) {
                continue;
            }
            
            int [] hyperSenior = new int [hyperSeniorCount];
            int [] fans = new int [fanCount];
            
            for (int i=0; i<hyperSeniorCount; i++) {
                hyperSenior[i] = hyperSeniorString.charAt(i) == 'M' ? 1 : 0;
            }
            
            for (int i=0; i<fanCount; i++) {
                fans[i] = fansString.charAt(i) == 'M' ? 1 : 0;
            }
            
            int hugCount = 0;
            for (int i=0; i<=fanCount-hyperSeniorCount; i++) {
                int handShake = 0;
                for (int j=0; j<hyperSeniorCount; j++) {
                    handShake += hyperSenior[j] & fans[i+j];
                }
                if (handShake == 0) {
                    hugCount++;
                }
            }
            
            System.out.println(hugCount);
        }
    }
}
