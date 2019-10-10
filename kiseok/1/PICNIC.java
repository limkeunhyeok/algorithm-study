package algo;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class PICNIC {
    private static int n;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int testCase = Integer.parseInt(br.readLine().trim());
        
        while (testCase-->0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            
            // 0 짝없음, 1 짝있음
            int [] match = new int[n];
            // 0 친구아님, 1 친구임
            int [][] friends = new int [n][n];
            
            for (int i=0; i<n; i++) {
                match[i] = 0;
                for (int j=0; j<n; j++) {
                    friends[i][j] = 0;
                }
            }
            
            st = new StringTokenizer(br.readLine());
            for (int i=0; i<m; i++) {
                 int first = Integer.parseInt(st.nextToken());
                 int second = Integer.parseInt(st.nextToken());
                 
                 friends[first][second] = 1;
                 friends[second][first] = 1;
            }
            
            friend(match, friends, 0);
            System.out.println(friend(match, friends, 0));
        }
    }
    
    private static int friend(int [] match, int [][] friends, int nextPerson) {
        int total=0;
        for (int i=0; i<n; i++) {
            total += match[i];
        }
        if (total == n) {
            return 1;
        }
        
        int result = 0;
        for (int i=nextPerson; i<n; i++) {
            if (match[i] == 1) {
                continue;
            } else {
                for (int j=i+1; j<n; j++) {
                    if (friends[i][j] == 1) {
                        if (match[j] == 1) {
                            continue;
                        } else {
                            match[i]=1; match[j]=1;
                            result += friend(match, friends, i+1);
                            match[i]=0; match[j]=0;
                        }
                    } else {
                        continue;
                    }
                }
            }
        }
        
        return result;
    }
}
