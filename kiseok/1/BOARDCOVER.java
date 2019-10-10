package algo;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOARDCOVER {
    static int H, W, result;
    static boolean[][] gameBoardcover;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int testCase = Integer.parseInt(br.readLine().trim());
        while (testCase-->0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            H = Integer.parseInt(st.nextToken());
            W = Integer.parseInt(st.nextToken());
            
            gameBoardcover = new boolean [H][W];
            
            int coverCount=0;
            for (int i=0; i<H; i++) {
                String line = br.readLine();
                for (int j=0; j<W; j++) {
                    if ("#".equals(line.substring(j, j+1))) {
                        gameBoardcover[i][j] = true; 
                    } else {
                        gameBoardcover[i][j] = false;
                        coverCount++;
                    }
                }
            }
            result = 0;
            if (coverCount%3 == 0) {
                result = getBoardCover(0, 0, coverCount);
            }
            System.out.println(result);
        }
        br.close();
    }
    
    private static int getBoardCover(int i, int j, int count) {
        if (count == 0) {
            return 1;
        }
        if (i==H) {
            return 0;
        }
        
        if (j==W) {
            return getBoardCover(i+1, 0, count);
        }
        
        if (gameBoardcover[i][j]) {
            return getBoardCover(i, j+1, count);
        }
        
        int result = 0;
        
        // **
        // *
        if (i+1 < H && j+1 < W && !gameBoardcover[i+1][j] && !gameBoardcover[i][j+1]) {
            gameBoardcover[i][j]=true; gameBoardcover[i+1][j]=true; gameBoardcover[i][j+1]=true;
            result += getBoardCover(i, j+1, count-3);
            gameBoardcover[i][j]=false; gameBoardcover[i+1][j]=false; gameBoardcover[i][j+1]=false;
        }
        
        // *
        // **
        if (i+1 < H && j+1 < W && !gameBoardcover[i+1][j] && !gameBoardcover[i+1][j+1]) {
            gameBoardcover[i][j]=true; gameBoardcover[i+1][j]=true; gameBoardcover[i+1][j+1]=true;
            result += getBoardCover(i, j+1, count-3);
            gameBoardcover[i][j]=false; gameBoardcover[i+1][j]=false; gameBoardcover[i+1][j+1]=false;
        }
        
        // **
        //  *
        if (i+1 < H && j+1 < W && !gameBoardcover[i][j+1] && !gameBoardcover[i+1][j+1]) {
            gameBoardcover[i][j]=true; gameBoardcover[i][j+1]=true; gameBoardcover[i+1][j+1]=true;
            result += getBoardCover(i, j+1, count-3);
            gameBoardcover[i][j]=false; gameBoardcover[i][j+1]=false; gameBoardcover[i+1][j+1]=false;
        }
        
        //  *
        // **
        if (i+1 < H && j-1 > 0 && !gameBoardcover[i+1][j] && !gameBoardcover[i+1][j-1]) {
            gameBoardcover[i][j]=true; gameBoardcover[i+1][j]=true; gameBoardcover[i+1][j-1]=true;
            result += getBoardCover(i, j+1, count-3);
            gameBoardcover[i][j]=false; gameBoardcover[i+1][j]=false; gameBoardcover[i+1][j-1]=false;
        }
        
        return result;
    }
    
    
    
    
    
//    public static void callGetBoardCover(boolean[][] gameBoardcover, int i, int j) {
//        if (j>=W-1) {
//            if (i>=H-1) {
//                boolean breakNow = false;
//                result++;
//                for (int ii=0; i<H; i++) {
//                    for (int jj=0; j<W; j++) {
//                        if (!gameBoardcover[ii][jj]) {
//                            breakNow=true;
//                            result--;
//                            break;
//                        }
//                    }
//                    if (breakNow) {
//                        break;
//                    }
//                }
//                return;
//            }
//            getBoardCover(gameBoardcover, i+1, 0);
//        }
//        getBoardCover(gameBoardcover, i, j+1);
//    }
//    
//    public static void getBoardCover(boolean[][] gameBoardcover, int i, int j) {
//        if (gameBoardcover[i][j]) {
//            if (j<W-1 && i<H-1 && gameBoardcover[i][j+1] && gameBoardcover[i+1][j]) {
//                gameBoardcover[i][j] = false;
//                gameBoardcover[i][j+1] = false;
//                gameBoardcover[i+1][j] = false;
//                callGetBoardCover(gameBoardcover, i, j);
//                gameBoardcover[i][j] = true;
//                gameBoardcover[i][j+1] = true;
//                gameBoardcover[i+1][j] = true;
//            }
//            if (j<W-1 && 1<=i && gameBoardcover[i][j+1] && gameBoardcover[i-1][j]) {
//                gameBoardcover[i][j] = false;
//                gameBoardcover[i][j+1] = false;
//                gameBoardcover[i-1][j] = false;
//                callGetBoardCover(gameBoardcover, i, j);
//                gameBoardcover[i][j] = true;
//                gameBoardcover[i][j+1] = true;
//                gameBoardcover[i-1][j] = true;
//                
//            }
//            if (1<=j && i<H-1 && gameBoardcover[i][j-1] && gameBoardcover[i+1][j]) {
//                gameBoardcover[i][j] = false;
//                gameBoardcover[i][j-1] = false;
//                gameBoardcover[i+1][j] = false;
//                callGetBoardCover(gameBoardcover, i, j);
//                gameBoardcover[i][j] = true;
//                gameBoardcover[i][j-1] = true;
//                gameBoardcover[i+1][j] = true;
//            }
//            if (1<=j && 1<=i && gameBoardcover[i][j-1] && gameBoardcover[i-1][j]) {
//                gameBoardcover[i][j] = false;
//                gameBoardcover[i][j+1] = false;
//                gameBoardcover[i-1][j] = false;
//                callGetBoardCover(gameBoardcover, i, j);
//                gameBoardcover[i][j] = true;
//                gameBoardcover[i][j+1] = true;
//                gameBoardcover[i-1][j] = true;
//                
//            }
//            
//            callGetBoardCover(gameBoardcover, i, j);
//        } else {
//            callGetBoardCover(gameBoardcover, i, j);
//        }
//    }
}
