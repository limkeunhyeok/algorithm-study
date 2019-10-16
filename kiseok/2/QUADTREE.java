package algo;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class QUADTREE {
    
    private static String input;
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int testCase = Integer.parseInt(br.readLine().trim());
        while (testCase-->0) {
            input = br.readLine();
            System.out.println(printQuadtree());
        }
    }
    
    private static String printQuadtree() {
        String [] result = new String [4];
        for (int i=0; i<4; i++) {
            result[i] = "";
        }
        
        int count=0;
        while (count < 4) {
            if (input.length() == 0) {
                break;
            }
            if (input.startsWith("w")) {
                input = input.substring(1);
                result[count] = "w";
                count++;
            } else if (input.startsWith("b")) {
                input = input.substring(1);
                result[count] = "b";
                count++;
            } else if (input.startsWith("x")) {
                input = input.substring(1);
                result[count] = "x" + printQuadtree();
                count++;
            }
        }
        
        return result[2] + result[3] + result[0] + result[1];
    }
}
