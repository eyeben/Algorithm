import java.io.*;
import java.util.*;

public class Main {


	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	int N = Integer.parseInt(st.nextToken());
    	int M = Integer.parseInt(st.nextToken());
    	int X = Integer.parseInt(st.nextToken());
    	
    	List<List<Integer>> left = new ArrayList<List<Integer>>();
    	List<List<Integer>> right = new ArrayList<List<Integer>>();
    	
    	for(int i = 0;i<N+1;i++) {
    		left.add(new ArrayList<Integer>());
    		right.add(new ArrayList<Integer>());
    	}
    	
    	
    	for(int i = 0; i < M;i++) {
    		st = new StringTokenizer(br.readLine());
    		int a = Integer.parseInt(st.nextToken());
    		int b = Integer.parseInt(st.nextToken());
    		
    		left.get(b).add(a);
    		right.get(a).add(b);
    	}
    	
    	int cnt = 0;
    	
    	boolean[] visited = new boolean[N+1];
    	Deque<Integer> dq = new ArrayDeque<>();
    	dq.add(X);
    	visited[X] = true;
    	while(!dq.isEmpty()) {
    		int node = dq.pollFirst();
    		for(int itm: left.get(node)) {
    			if(visited[itm])
    				continue;
    			visited[itm] = true;
    			cnt++;
    			dq.add(itm);
    		}
    	}
    	int ans1 = cnt + 1;
    	
    	visited = new boolean[N+1];
    	dq = new ArrayDeque<>();
    	dq.add(X);
    	visited[X] = true;
    	while(!dq.isEmpty()) {
    		int node = dq.pollFirst();
    		for(int itm: right.get(node)) {
    			if(visited[itm])
    				continue;
    			visited[itm] = true;
    			cnt++;
    			dq.add(itm);
    		}
    	}
    	int piv = N - 1 - cnt;
    	System.out.println(ans1+" "+ (ans1+piv));
    
	}



}