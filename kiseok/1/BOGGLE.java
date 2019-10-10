package algo;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BOGGLE {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int testCase = Integer.parseInt(br.readLine().trim());
        
        char [][] array_word = new char[5][5];
        while(testCase-->0) {
            for (int i=0; i<5; i++) {
                String line = br.readLine();
                for (int j=0; j<5; j++) {
                    array_word[i][j] = line.charAt(j);
                }
            }
            
            int N = Integer.parseInt(br.readLine().trim());
            for (int i=0; i<N; i++) {
                String line = br.readLine();

                boolean result = false;
                for (int j=0; j<N; j++) {
                    for (int k=0; k<N; k++) {
                        if(isBoggle(line, array_word, j, k)) {
                            result = true;
                            break;
                        }
                    }
                    if (result) {
                        break;
                    }
                }
                System.out.println(result);
            }
        }
    }
    
    private static boolean isBoggle(String word, char[][] array_word, int x, int y) {
        if (x<0 || x>=5 || y<0 || y>=5) {
            return false;
        }
        if (array_word[x][y] != word.charAt(0)) {
            return false;
        }
        if (word.length() == 1) {
            return true;
        }
        
        String nextWord = word.substring(1);
        
        return isBoggle(nextWord, array_word, x-1, y-1) || isBoggle(nextWord, array_word, x-1, y) || isBoggle(nextWord, array_word, x-1, y+1) ||
        isBoggle(nextWord, array_word, x, y-1) || isBoggle(nextWord, array_word, x, y+1) ||
        isBoggle(nextWord, array_word, x+1, y-1) || isBoggle(nextWord, array_word, x+1, y) || isBoggle(nextWord, array_word, x+1, y+1);
    }
}
