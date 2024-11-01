import java.io.*;
import java.util.*;

public class Main {

	static final int BIG = Integer.MAX_VALUE;

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		
		for(int t = 0; t < T ; t++) {
			st = new StringTokenizer(br.readLine());

            int N = Integer.parseInt(st.nextToken()); // 노드 수
            int D = Integer.parseInt(st.nextToken()); // 간선 수
            int C = Integer.parseInt(st.nextToken());
		
			List<List<int[]>> graph = new ArrayList<>();
			
			for (int i = 0; i< N+1;i++)
				graph.add(new ArrayList<>());
			
			for (int i = 0; i < D; i++) {
	            st = new StringTokenizer(br.readLine());
	            int a = Integer.parseInt(st.nextToken());
	            int b = Integer.parseInt(st.nextToken());
	            int c = Integer.parseInt(st.nextToken());
	            graph.get(b).add(new int[]{a, c});
	        }
			
			int[] distances = new int[N+1];
			Arrays.fill(distances, BIG);
			PriorityQueue<int[]> pq = new PriorityQueue<>((o1,o2)->o1[1] - o2[1]);
			pq.add(new int[] {C, 0});
			distances[C] = 0;
			
			
			while(!pq.isEmpty()) {
				int[] tmp = pq.poll();
				int node = tmp[0];
				int dist = tmp[1];
				
				for(int[] itm: graph.get(node)) {
					int nextNode = itm[0];
					int nextDist = itm[1];
					
					if(nextDist + dist < distances[nextNode]) {
						pq.add(new int[] {nextNode, nextDist + dist});
						distances[nextNode] = nextDist + dist;
					}
				}
				
				
			}
			int ans1 = 0;
			int ans2 = 0;
			for(int i = 1; i<N+1;i++)
				if (distances[i] != BIG) {
					ans1++;
					ans2 = Math.max(distances[i], ans2);
				}
			
			System.out.println(ans1+" "+ans2);
		}
	}

}