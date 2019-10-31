package algo;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class JLIS {
    private static int N, M;
    private static int [] array1;
    private static int [] array2;
    private static int [][] biggestLISLength;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int testCase = Integer.parseInt(br.readLine().trim());
        while (testCase-->0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            
            array1 = new int [N];
            st = new StringTokenizer(br.readLine());
            for (int i=0; i<N; i++) {
                array1[i] = Integer.parseInt(st.nextToken());
            }
            
            array2 = new int [M];
            st = new StringTokenizer(br.readLine());
            for (int i=0; i<M; i++) {
                array2[i] = Integer.parseInt(st.nextToken());
            }
            biggestLISLength = new int [N][M];
            for (int i=0; i<N; i++) {
                for (int j=0; j<M; j++) {
                    biggestLISLength[i][j] = 0;
                }
            }

            for (int i=N-1; i>=0; i--) {
                for (int j=M-1; j>=0; j--) {
                    getBiggestLISLength(i, j);
                }
            }
            
            for (int i=0; i<N; i++) {
                for (int j=0; j<M; j++) {
                    System.out.print(biggestLISLength[i][j] + " ");
                }
                System.out.println();
            }
            System.out.println();
        }
    }
    
    
    private static int getBiggestLISLength(int index1, int index2) {
        if (biggestLISLength[index1][index2] != 0) {
            return biggestLISLength[index1][index2];
        }
        
        boolean isMax = true;
        for (int i=index1+1; i<N; i++) {
            isMax = isMax & (array1[index1] > array1[i]);
        }
        for (int i=index2+1; i<M; i++) {
            isMax = isMax & (array2[index2] > array2[i]);
        }
        if (isMax) {
            if(array1[index1] == array2[index2]) {
                biggestLISLength[index1][index2] = 1;
                return 1;
            } else {
                biggestLISLength[index1][index2] = 2;
                return 2;
            }
        }
        
        int maxLIS=2;
        int bigNum = Math.max(array1[index1], array2[index2]);
        for (int i=index1+1; i<N; i++) {
            if (array1[index1] < array1[i]) {
                maxLIS = Math.max(maxLIS, getBiggestLISLength(i, index2)+1);
                if (array2[index2] == array1[index1]) {
                    maxLIS--;
                }
            }
        }
        for (int i=index2+1; i<M; i++) {
            if (array2[index2] < array2[i]) {
                maxLIS = Math.max(maxLIS, getBiggestLISLength(index1, i)+1);
                if (array1[index1] == array2[index2]) {
                    maxLIS--;
                }
            }
        }
        biggestLISLength[index1][index2] = maxLIS;
        return maxLIS;
    }
}
