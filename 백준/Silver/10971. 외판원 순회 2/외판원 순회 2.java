import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int [] arr;
    static int N;
    static int[][] bd;
    static int mn;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        bd = new int[N][N];
        for(int i =0 ;i< N;i++){
            st = new StringTokenizer(br.readLine());
            for(int j =0; j< N; j++)
                bd[i][j] = Integer.parseInt(st.nextToken());
        }
        arr = new int[N];
        for(int i =0; i<N;i++)
            arr[i] = i;
        mn = Integer.MAX_VALUE;
        perm(1);
        System.out.println(mn);
    }

    private static void swap(int a, int b){
        int tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
    }

    private static void perm(int depth){
        if(depth == N){
            int total = 0;
            int prevNode = 0;
            for(int i = 1;i<N;i++){
                if(bd[prevNode][arr[i]] == 0)
                    return;
                total+= bd[prevNode][arr[i]];
                prevNode = arr[i];
            }
            if(bd[prevNode][0] == 0)
                return;

            total += bd[prevNode][0];
            mn = Math.min(mn, total);

            return;
        }

        for(int i = depth; i<N;i++){
            swap(i, depth);
            perm(depth+1);
            swap(i, depth);
        }
    }


}