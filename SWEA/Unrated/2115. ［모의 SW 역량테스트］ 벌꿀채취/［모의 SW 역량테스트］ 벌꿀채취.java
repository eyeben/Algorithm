import java.io.*;
import java.util.*;

public class Solution {
    static int N;
    static int M;
    static int C;
    static int[][] bd;
    static int mx;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());

        for(int tc= 1; tc<=T; tc++){
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());

            bd = new int[N][N];
            for(int i = 0; i < N; i++){
                st = new StringTokenizer(br.readLine());
                for(int j = 0; j < N; j++)
                    bd[i][j] = Integer.parseInt(st.nextToken());
            }

            List<List<Integer>> bd2 = new ArrayList<>();
            for(int i = 0; i < N; i++) {
                bd2.add(new ArrayList<>());
                for (int j = 0; j <= N - M; j++)
                    bd2.get(i).add(getVal(j,i));

            }

            int ans = 0;
            for(int i =0; i < N -1 ; i++){
                int tmp = Collections.max(bd2.get(i));
                for(int j = i+1; j<N; j++)
                    ans = Math.max(Collections.max(bd2.get(j))+tmp,ans);
            }
            for(int row = 0; row<N;row ++)
                for (int i = 0; i <= N - M - 1; i++)
                    for (int j = i + M; j <= N - M; j++)
                        ans = Math.max(ans, bd2.get(row).get(i) + bd2.get(row).get(j));

            bw.append(String.format("#%d %d\n",tc,ans));
        }
        bw.close();
    }
    private static int getVal(int x, int y){

        List<Integer>li = new ArrayList<>();
        int total = 0;
        for(int i = 0; i< M;i++){
            total += bd[y][x+i];
            li.add(bd[y][x+i]);
        }

        mx = 0;
        visited = new boolean[M];
        booboon(0, li);

        return mx;

    }

    private static void booboon(int idx, List<Integer>li){
        if(idx == M) {
            int total = 0;
            for (int i = 0; i < M; i++)
                if (visited[i])
                    total += li.get(i);

            if (total <= C) {
                int total2 = 0;
                for (int i = 0; i < M; i++)
                    if (visited[i])
                        total2 += (int) Math.pow(li.get(i), 2);
                mx = Math.max(total2, mx);
            }

            return;
        }

        visited[idx] = true;
        booboon(idx + 1, li);
        visited[idx] = false;
        booboon((idx + 1), li);
    }
}