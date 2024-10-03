import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T =Integer.parseInt(br.readLine());
		for(int tc = 1; tc<=T; tc++ ) {
			int N = Integer.parseInt(br.readLine());
			int[] li = new int[N];
			st = new StringTokenizer(br.readLine());
			for(int i = 0;i<N;i++)
				li[i] = Integer.parseInt(st.nextToken());
			List<Integer> lis = new ArrayList<>();
			lis.add(li[0]);
			
			for(int i = 1;i<N;i++) {
				int num = li[i];
				if(lis.get(lis.size()-1) <= num)
					lis.add(num);
				else {
					int left = 0;
					int right = lis.size()-1;
					int idx = 0;
					while(left<=right) {
						int mid = (int)(left+right)/2;
						if (num <= lis.get(mid)) {
							idx = mid;
							right = mid - 1;
							
						}
						else
							left = mid+1;
					}
					
					lis.set(idx, num);


				}
			}
			System.out.printf("#%d %d\n",tc,lis.size());
		}

	}

}