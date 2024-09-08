import java.io.*;
import java.util.*;

public class Solution {
    static int N;
    static int cnt;
    static int[][] adjs;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        for(int tc = 1; tc<=T; tc++){
            N = Integer.parseInt(br.readLine());
            int M = Integer.parseInt(br.readLine());
            adjs = new int[N+1][N+1];
            for (int i =0;i <M; i++){
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                adjs[a][b] = 1;
            }

            for (int i = 1; i< N+1;i++)
                adjs[i][0] = -1;
            for(int i =1; i< N+1;i++){
                if(adjs[i][0]!=-1)
                    continue;
                dfs(i);
            }
            for(int i = 1;i<N+1;i++)
                for(int j = 1; j<N+1;j++)
                    adjs[0][j] += adjs[i][j];

            int ans = 0;
            for (int i = 1;i<N+1;i++)
                if(adjs[i][0] + adjs[0][i] == N-1)
                    ans++;
            System.out.printf("#%d %d\n",tc,ans);
        }
    }
    static void dfs(int cur){
        for (int i =1;i<=N;i++){
            if(adjs[cur][i] == 0)
                continue;
            if(adjs[i][0] == -1)
                dfs(i);

            if(adjs[i][0]>0)
                for(int j = 1; j<=N; j++)
                    if(adjs[i][j]!= 0)
                        adjs[cur][j] =1;
        }
        adjs[cur][0] = 0;
        for(int i=1;i<=N;i++)
            adjs[cur][0] += adjs[cur][i];
    }

}