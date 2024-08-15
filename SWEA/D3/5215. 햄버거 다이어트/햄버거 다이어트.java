import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {

    static int mx;
    static Integer[][] arr;
    static boolean[] visited;
    static int N;
    static int L;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        for(int tc = 1; tc<=T;tc++){
            mx = 0;
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            L = Integer.parseInt(st.nextToken());

            arr = new Integer[N][2];
            visited = new boolean[N];


            for(int i = 0 ; i < N;i++){
                st = new StringTokenizer(br.readLine());
                arr[i][0] = Integer.parseInt(st.nextToken());
                arr[i][1] = Integer.parseInt(st.nextToken());
            }
            for(int i = 0;i<=N;i++)
                combination(0,i);
            System.out.printf("#%d %d\n",tc,mx);
        }

    }

    private static void combination( int start, int r){
        if(r==0){
            int happy = 0, calories = 0;
            for(int i =0;i<N;i++)
                if(visited[i]) {
                    happy += arr[i][0];
                    calories += arr[i][1];
                }
            mx = calories <= L ? Math.max(mx, happy):mx;
            return;
        }

        for(int i = start; i<N;i++){
            visited[i] = true;
            combination(i+1, r-1);
            visited[i] = false;
        }

    }


}