package algo;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class TRIANGLEPATH {
    private static int[][] triangleBoard;
    private static int[][] biggestSum;
    private static int n;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int testCase = Integer.parseInt(br.readLine().trim());
        while (testCase-->0) {
            n = Integer.parseInt(br.readLine().trim());
            
            triangleBoard = new int[n][n];
            biggestSum = new int[n][n];
            
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j <= i; j++) {
                    triangleBoard[i][j] = Integer.parseInt(st.nextToken());
                    biggestSum[i][j] = -1;
                }
            }
            
            System.out.println(getBiggestSum(0, 0));
        }
    }
    
    private static int getBiggestSum(int i, int j) {
        if (i == n-1) {
            return triangleBoard[i][j];
        }

        if (biggestSum[i][j] != -1) {
            return biggestSum[i][j];
        }
        
        int result = triangleBoard[i][j] + Math.max(getBiggestSum(i+1, j), getBiggestSum(i+1, j+1));
        
        biggestSum[i][j] = result;
        
        return result;
    }
}
