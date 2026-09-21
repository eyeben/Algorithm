#include <string>
#include <vector>
#include <deque>
#include <iostream>
using namespace std;
int INF = 1e9;
int solution(vector<string> board) {
    int N = board.size();
    int M = board[0].size();
    vector <vector<int>> bd(N, vector<int>(M, INF));
    
    int RX = 0, RY = 0;
    int GX = 0, GY = 0;
    
    for(int y = 0; y < N; y++){
        for(int x = 0; x < M; x++){
            if (board[y][x] == 'R'){
                RX = x;
                RY = y;
                bd[y][x] = 0;
            }
            else if (board[y][x] == 'G'){
                GX = x;
                GY = y;
            }
        }
    }
    
    vector<int> dx = {0,1,0,-1};
    vector<int> dy = {1,0,-1,0};
    
    deque<tuple<int, int, int>> dq;
    dq.push_back({RX,RY,0});
    
    while (!dq.empty()){
        auto [x,y,dist] = dq.front();
        dq.pop_front();
        for(int i = 0; i < 4; i++){
            int nx = x, ny = y;
            while(true){
                if(0 <= nx+dx[i] and nx+dx[i]< M and 0 <= ny+dy[i] and ny+dy[i] < N and board[ny+dy[i]][nx+dx[i]] != 'D'){
                    nx += dx[i];
                    ny += dy[i];
                }
                else{
                    break;
                }
            }
            if (bd[ny][nx] > dist + 1){
                bd[ny][nx] = dist + 1;
                dq.push_back({nx,ny,dist + 1});
            }
                
        }
    }
    return bd[GY][GX] == INF ? -1 : bd[GY][GX];
}