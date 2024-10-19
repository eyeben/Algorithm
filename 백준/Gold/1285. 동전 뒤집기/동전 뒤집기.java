import java.io.*;
import java.util.*;

public class Main {

	static int N;
	static boolean[][] bd;
	static int ans;
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		bd = new boolean[N][N]; 
		for(int i =0 ;i<N;i++) {
			String str = br.readLine();
			for(int j =0;j<N;j++)
				bd[i][j] = str.charAt(j) == 'H' ? true:false;
		}
		ans =0;
		for(int i =0 ;i<N;i++)
			for(int j =0;j<N;j++)
				ans+= bd[i][j] ? 1 : 0;
		
		dfs(0);
		System.out.println(ans);
	}
	
	private static void dfs(int idx) {
		if(idx == N) {
			int total = 0;
			for(int i = 0;i < N;i++) {
				int tmp = 0;
				for(int j = 0;j<N;j++)
					tmp += bd[i][j] ? 1 : 0;
				total += Math.min(tmp, N-tmp);
			}
			ans = Math.min(ans, total);
			return;
		}
		
		dfs(idx+1);
		
		for(int i = 0; i < N; i++)
			bd[i][idx] = !bd[i][idx]; 

		dfs(idx+1);	
	}
}