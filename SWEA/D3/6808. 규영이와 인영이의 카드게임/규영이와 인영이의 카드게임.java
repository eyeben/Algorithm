import java.io.*;
import java.util.*;
 
public class Solution {
    static List<Integer> cards1 = new ArrayList<>();
    static List<Integer> cards2 = new ArrayList<>();
    static int winCnt = 0;
    static int loseCnt = 0; 
 
    public static void main(String[] args) throws NumberFormatException, IOException {
         
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
         
        for(int t = 1;t<=N;t++) {
            winCnt = 0;
            loseCnt = 0;
            cards1 = new ArrayList<>();
            cards2 = new ArrayList<>();
             
            st = new StringTokenizer(br.readLine());
            boolean[] nums = new boolean[19];
            for(int i =0; i<9;i++) {
                cards1.add(Integer.parseInt(st.nextToken()));
                nums[cards1.get(i)] = true;
            }
         
        for(int i =1; i<19;i++)
            if(!nums[i])
                cards2.add(i);
         
        permutation(0);
        System.out.printf("#%d %d %d\n", t, winCnt, loseCnt);
         
        }
         
         
    }
    static void swap(int idx1, int idx2) {
        int tmp = cards2.get(idx1);
        cards2.set(idx1, cards2.get(idx2));
        cards2.set(idx2, tmp);
    }
     
     
    static void permutation(int depth) {
        if (depth == 9) {
            dual();
            return;
        }
         
        for(int i = depth; i<9;i++) {
            swap(depth,i);
            permutation(depth+1);
            swap(depth,i);
        }
         
    }
     
    static void dual() {
        int cnt1 = 0, cnt2 = 0, ans = 0;
         
        for(int i = 0;i < 9;i++) {
            if(cards1.get(i) < cards2.get(i))
                cnt2+= cards1.get(i) + cards2.get(i);
            else
                cnt1+= cards1.get(i) + cards2.get(i);
        }
        
        ans = cnt2-cnt1;
        if(ans < 0)
            winCnt++;
        else if(ans > 0)
            loseCnt++;
         
    }
 
}