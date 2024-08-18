import java.io.*;
import java.util.*;

public class Solution {

    static int[] pairs;
    static boolean[] visited;
    static int N;
    static int M;
    static int ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        for(int tc = 1; tc<=T;tc++){
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            pairs = new int[N+1];

            visited = new boolean[N+1];
            ans = 0;

            for(int i = 0 ; i < M;i++){
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                pairs[a] = pairs[a]|(1<<b);
                pairs[b] = pairs[b]|(1<<a);
            }

            // 조합은 0부터 N개까지
            for(int i = 0;i<=N;i++)
                combination(1,i);
            System.out.printf("#%d %d\n",tc, ans);
        }

    }
    private static void combination( int start, int r){
    	// 새로운 조합이 형성 될 때 마다 체크
        if(!check())
            return;
        
        if(r==0){
            ans++;
            return;
        }
        // 새로운 조합 생성
        for(int i = start; i<N+1;i++){
            visited[i] = true;
            combination(i+1, r-1);
            visited[i] = false;
        }
    }
    // 비트마스킹을 이용한 페어 검사
    private static boolean check() {
    	// 현재 조합에서 존재하는 번호를 1로 표시한다
    	int bit = 1 << (N + 1);
    	for(int i = 1; i < N+1; i++) {
    		if(visited[i])
    			bit = bit | (1<<i);
    	}
    	// 같이 넣으면 안되는 번호가 존재 하는지 확인
    	for(int i = 1; i < N+1; i++)
    		if(visited[i])
				// 현재 조합에 넣으면 안되는 재료가 있는지 확인
				if((bit & pairs[i]) != 0)
					return false;

    	return true;
    }
}