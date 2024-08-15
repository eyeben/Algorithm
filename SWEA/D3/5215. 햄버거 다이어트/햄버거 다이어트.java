import java.io.*;
import java.util.*;

public class Solution {

    static int mx;
    static int[][] arr;
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

            arr = new int[N][2];
            visited = new boolean[N];


            for(int i = 0 ; i < N;i++){
                st = new StringTokenizer(br.readLine());
                arr[i][0] = Integer.parseInt(st.nextToken());
                arr[i][1] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(arr, (o1,o2)->(o1[1] - o2[0]));
            // 조합은 0부터 N개까지
            for(int i = 0;i<=N;i++)
                combination(0,i,0,0);
            System.out.printf("#%d %d\n",tc,mx);
        }

    }
    // 재귀와 visited를 이용한 조합 구현
    private static void combination( int start, int r, int currentCalories, int currentHappiness){
        // 칼로리 초과시 더 이상 할 이유가 없음
        if(currentCalories > L)
            return;
        // 조합이 다 찼을 경우 -> mx 최댓값 갱신
        if(r==0){
            mx = Math.max(mx, currentHappiness);
            return;
        }
        // 조합을 저 채워야 하는 경우
        for(int i = start; i<N;i++){
            visited[i] = true;
            combination(i+1, r-1, currentCalories + arr[i][1], currentHappiness+arr[i][0]);
            visited[i] = false;
        }

    }


}