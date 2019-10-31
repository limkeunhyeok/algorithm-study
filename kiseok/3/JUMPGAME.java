package algo;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class JUMPGAME {
    private static int[][] canJump;
    private static int[][] jumpBoard;
    private static int n;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCase = Integer.parseInt(br.readLine().trim());
        while (testCase-- > 0) {
            n = Integer.parseInt(br.readLine().trim());

            jumpBoard = new int[n][n];
            canJump = new int[n][n];
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    jumpBoard[i][j] = Integer.parseInt(st.nextToken());
                    canJump[i][j] = -1;
                }
            }
            if (jumpGame(0, 0)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }

    private static boolean jumpGame(int i, int j) {
        if (i >= n || j >= n) {
            return false;
        }
        if (i == n-1 && j == n-1) {
            return true;
        }
        
        if (canJump[i][j] == 1) {
            return true;
        } else if (canJump[i][j] == 0) {
            return false;
        }

        int distance = jumpBoard[i][j];
        boolean result = jumpGame(i + distance, j) | jumpGame(i, j + distance);
        
        if (result) {
            canJump[i][j] = 1;
        } else {
            canJump[i][j] = 0;
        }
        
        return result;
    }
}
