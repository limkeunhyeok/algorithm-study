package nhn2018;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No1 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        
        int [][] city = new int[n][m];
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                // 1=운행안됨, 0=운행됨
                city[i][j]=1;
            }
        }
        
        while(k-->0) {
            st = new StringTokenizer(br.readLine());
            
            int r = Integer.parseInt(st.nextToken());
            int c1 = Integer.parseInt(st.nextToken());
            int c2 = Integer.parseInt(st.nextToken());
            
            for (int i=c1-1; i<=c2-1; i++) {
                city[r-1][i]=0;
            }
        }
        
        int result = 0;
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                result += city[i][j];
            }
        }
        
        System.out.println(result);
    }
}
