package algo;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class LIS {
    private static int N;
    private static int [] array;
    private static int [] biggestLISLength;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int testCase = Integer.parseInt(br.readLine().trim());
        while (testCase-->0) {
            N = Integer.parseInt(br.readLine().trim());
            
            array = new int [N];
            biggestLISLength = new int [N];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i=0; i<N; i++) {
                array[i] = Integer.parseInt(st.nextToken());
                biggestLISLength[i] = 0;
            }
            int result =0;
            for (int i=0; i<N; i++) {
                result = Math.max(result, getBiggestLISLength(i));
            }
            System.out.println(result);
        }
    }
    
    private static int getBiggestLISLength(int index) {
        if (index>=N) {
            return 0;
        }
        if (biggestLISLength[index] != 0) {
            return biggestLISLength[index];
        }
        
        boolean isMax = true;
        for (int i=index+1; i<N; i++) {
            isMax = isMax & (array[index] > array[i]);
        }
        if (isMax) {
            return 1;
        }
        
        int maxLIS=0;
        for (int i=index+1; i<N; i++) {
            if (array[index] < array[i]) {
                maxLIS = Math.max(maxLIS, getBiggestLISLength(i));
            }
        }
        biggestLISLength[index] = maxLIS + 1;
        return maxLIS + 1;
    }
}
