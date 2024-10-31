import java.util.*;
class Solution {
    int[] dx = new int[]{0,1,0,-1};
    int[] dy = new int[]{1,0,-1,0};
    int N = 0;
    int M = 0;
    public int solution(int[][] land) {
        N = land.length;
        M = land[0].length;
        int[] answers = new int[M];
        
        for(int i = 0; i < N ;i++)
            for(int j = 0; j< M; j++)
                if(land[i][j] == 1)
                    bfs(land, answers, j, i);
        int answer = 0;
        for(int itm:answers)
            answer = Math.max(itm, answer);
        
        return answer;
    }
    private void bfs(int[][] land, int[] answers, int sx, int sy){
        Deque<int[]> dq = new ArrayDeque<>();
        land[sy][sx] = 0;
        dq.addFirst(new int[]{sx, sy});
        int mn = sx;
        int mx = sx;
        int cnt = 1;
        while(!dq.isEmpty()){
            int[] xy = dq.pollFirst();
            for(int i = 0; i < 4; i++){
                int nx = xy[0]+dx[i];
                int ny = xy[1]+dy[i];
                
                if(nx<0 || ny <0 || M<=nx || N<=ny)
                    continue;
                if(land[ny][nx] == 1){
                    cnt++;
                    land[ny][nx] = 0;
                    mx = Math.max(nx,mx);
                    mn = Math.min(nx,mn);
                    dq.addLast(new int[]{nx,ny});
                }
            }
        }
        
        for(int i = mn; i<=mx;i++)
            answers[i] += cnt;
    }
}