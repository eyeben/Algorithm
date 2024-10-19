import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	int N = Integer.parseInt(st.nextToken());
    	int K = Integer.parseInt(st.nextToken());
    	st = new StringTokenizer(br.readLine());
    	LinkedList<Integer> ll = new LinkedList<>();
    	
    	for(int i = 0; i<N*2;i++)
    		ll.add(Integer.parseInt(st.nextToken()));
    		
    	int cnt = 0;
    	
    	for(int itm: ll)
    		if(itm == 0)
    			cnt++;
    	int step = 0;
    	boolean[] robotAt = new boolean[N];
    	while (cnt<K) {
	    	// 로봇 회전
			for(int i = N - 1; i >= 1; i--)
				robotAt[i] = robotAt[i-1];
			robotAt[0]=false;
			robotAt[N-1] = false;
    		// 벨트 회전
    		ll.addFirst(ll.pollLast());
    		
    		// 로봇이동
    		for(int i = N - 1;i >= 1;i--) { 
    			if(robotAt[i] == true)
    				continue;
    			if(robotAt[i-1] && ll.get(i) > 0) {
    				robotAt[i-1]= false;
    				robotAt[i] = true;
    				ll.set(i, ll.get(i) - 1);
    				if(ll.get(i) == 0)
    					cnt++;
    			}
    		}
    
    		// 로봇 올리기
    		if(ll.get(0) != 0 && !robotAt[0]) {
	    		robotAt[0] = true;
	    		ll.set(0, ll.get(0)-1);
	    		if(ll.get(0) == 0)
	    			cnt++;
    		}
    		
    		step++;

    	}
    	System.out.println(step);
    }
}
