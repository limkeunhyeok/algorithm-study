package algo;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class FENCE {
    private static int [] fences;
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int testCase = Integer.parseInt(br.readLine().trim());
        while (testCase-->0) {
            int N = Integer.parseInt(br.readLine().trim());
            StringTokenizer st = new StringTokenizer(br.readLine());
            fences = new int [N];
            for (int i=0; i<N; i++) {
                fences[i] = Integer.parseInt(st.nextToken());
            }
            
            int result=getMaxArea(0, N-1);
            System.out.println(result);
        }
        br.close();
    }
    

    private static int getMaxArea (int startIndex, int endIndex) {
        
        if (startIndex == endIndex) {
            return fences[startIndex];
        }
        int mid = (startIndex + endIndex)/2;
        int leftMaxArea = getMaxArea(startIndex, mid);
        int rightMaxArea = getMaxArea(mid+1, endIndex);
        
        int maxArea = leftMaxArea > rightMaxArea ? leftMaxArea : rightMaxArea;
        
        int left = mid, right = mid+1;
        int height= fences[left] > fences[right] ? fences[right] : fences[left];
        int middleMaxArea = height * 2;
        
        while ((startIndex < left) && (right < endIndex)) {
            if ((fences[left-1] > fences[right+1])) {
                left--;
                height = height < fences[left] ? height : fences[left];
            } else {
                right++;
                height = height < fences[right] ? height : fences[right];
            }
            middleMaxArea = middleMaxArea > height*(right-left+1) ? middleMaxArea : height*(right-left+1);
        }
        
        while (startIndex < left) {
            left--;
            height = height < fences[left] ? height : fences[left];
            middleMaxArea = middleMaxArea > height*(right-left+1) ? middleMaxArea : height*(right-left+1);
        }
        
        while (right < endIndex) {
            right++;
            height = height < fences[right] ? height : fences[right];
            middleMaxArea = middleMaxArea > height*(right-left+1) ? middleMaxArea : height*(right-left+1);
        }
        
        maxArea = maxArea > middleMaxArea ? maxArea : middleMaxArea;
        
        return maxArea;
    }
}
