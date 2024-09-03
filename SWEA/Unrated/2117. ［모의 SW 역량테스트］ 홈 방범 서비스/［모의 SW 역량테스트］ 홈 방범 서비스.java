import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;


        int T = Integer.parseInt(br.readLine());

        for (int tc = 1;tc <=T; tc++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            int[][] li = new int[N][N];
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    li[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int ans = N;

            int[] dx = {0, 1, 0, -1};
            int[] dy = {-1, 0, 1, 0};

            int mx = 0;

            for (int dist = N +1; dist > 0; dist--) {
                boolean goodFlag = false;
                for (int i = 0; i < N; i++) {
                    for (int j =0; j < N; j++) {
                        int tmpcnt = man(j, i, dist, li, N);
                        if (tmpcnt* M >= dist * dist + (dist - 1) * (dist - 1)) {
                            goodFlag = true;
                            mx = Math.max(mx, tmpcnt);
                        }
                    }
                }
                if (goodFlag) {
                    break;
                }
            }
            sb.append("#").append(tc).append(" ").append(mx).append("\n");
        }

        System.out.print(sb.toString());
    }

    public static int man(int sx, int sy, int dist, int[][] li, int N) {
        int cnt = 0;
        for (int i = Math.max(0, sx - dist - 1); i < Math.min(sx + dist + 1, N); i++) {
            for (int j = Math.max(0, sy - dist); j < Math.min(sy + dist + 1, N); j++) {
                if (Math.abs(i - sx) + Math.abs(j - sy) < dist) {
                    cnt += li[j][i];
                }
            }
        }
        return cnt;
    }
}