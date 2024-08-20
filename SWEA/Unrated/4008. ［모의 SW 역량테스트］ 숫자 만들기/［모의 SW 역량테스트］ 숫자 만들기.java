import java.io.*;
import java.util.*;

public class Solution {
    static int mx;
    static int mn;
    static int N;
    static int[] coms;
    static int[] nums;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        for(int tc = 1; tc<=T;tc++) {
            mn = 100_000_001;
            mx = -100_000_001;
            N = Integer.parseInt(br.readLine());

            coms = new int[4];
            nums = new int[N];

            st = new StringTokenizer(br.readLine());
            for(int i = 0;i<4;i++)
                coms[i] = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            for(int i = 0;i<N;i++)
                nums[i] = Integer.parseInt(st.nextToken());

            dfs(1, nums[0]);
            System.out.printf("#%d %d\n",tc ,mx - mn);
        }
    }
    private static void dfs(int depth, int currentValue){
        if (depth == N){
            mx = Math.max(mx, currentValue);
            mn = Math.min(mn, currentValue);
            return;
        }

        for(int i = 0;i<4;i++){
            if(coms[i] == 0)
                continue;
            coms[i]--;
            if(i == 0)
                dfs(depth + 1, currentValue + nums[depth]);
            else if(i == 1)
                dfs(depth + 1, currentValue - nums[depth]);
            else if(i  == 2)
                dfs(depth + 1, currentValue * nums[depth]);
            else
                dfs(depth + 1, currentValue / nums[depth]);
            coms[i]++;
        }

    }


}