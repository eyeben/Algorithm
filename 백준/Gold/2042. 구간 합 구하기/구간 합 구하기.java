import java.io.*;
import java.util.*;

public class Main {
	static int size;
	static int N;
	static int M;
	static int K;
	static long[] tree;
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	N = Integer.parseInt(st.nextToken());
    	M = Integer.parseInt(st.nextToken());
    	K = Integer.parseInt(st.nextToken());

    	
    	size = 1;
    	while (size <N)
    		size <<= 1;
    	tree = new long[2*size];
    	size--;
    	
    	for(int i = 1;i<N+1;i++)
    		update(i,Long.parseLong(br.readLine()));
    	
    	for(int i = 0;i<M+K;i++) {
    		st = new StringTokenizer(br.readLine());
    		int a = Integer.parseInt(st.nextToken());
    		int b = Integer.parseInt(st.nextToken());
    		long c = Long.parseLong(st.nextToken());
    		
    		if(a == 1)
    			update(b,c-tree[b+size]);
    		else if(a == 2)
    			System.out.println(query(b,(int)c));
    	}
    		
    	
    
	}
	static long query(int left, int right) {
		left += size;
		right += size;
		long ans = 0;
		
		while (left<=right) {
			if (left%2 ==1) {
				ans += tree[left];
				left += 1;
			}
			left /= 2;
			
			if (right%2 == 0) {
				ans += tree[right];
				right -= 1;
			}
			right /= 2;
		}
		return ans;
	}
	
	
	
	static void update(int idx, long diff) {
		idx += size;
		while (idx > 0) {
			tree[idx] += diff;
			idx /= 2;
		}
	}

}