import java.io.*;
import java.util.*;

public class Main {
    static int[] parents;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        List<int[]> li = new ArrayList<>();
        for (int i = 0 ; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j<N; j++){
                int n = Integer.parseInt(st.nextToken());
                li.add(new int[]{n, i, j});
            }
        }

        parents = new int[N];
        for(int i =0; i<N;i++){
            parents[i]= i;
        }
        li.sort(Comparator.comparingInt(x->x[0]));

        long ans = 0;
        int cnt = 0;
        for(int[] edge:li){
            int a = edge[1];
            int b = edge[2];
            if(findParent(parents[a]) != findParent(parents[b])){
                union(a,b);
                ans += edge[0];
                if(++cnt == N)
                    break;
            }
        }
        System.out.println(ans);

    }
    private static int findParent(int n){
        if (parents[n] != n)
            parents[n] = findParent(parents[n]);
        return parents[n];
    }

    private static void union(int a,int b){
        a = findParent(a);
        b = findParent(b);
        if(a<b)
            parents[a] = b;
        else if (a>b)
            parents[b] = a;
    }

}