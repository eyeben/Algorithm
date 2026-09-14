#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int solution(int n, int k, vector<int> enemy) {
    priority_queue<int> maxHeap;
    int cur = n;
    for(int i = 0; i < enemy.size(); i++){
        
        maxHeap.push(enemy[i]);
        cur -= enemy[i];

        if (cur < 0 and k > 0){
            k--;
            cur += maxHeap.top();
            maxHeap.pop();
        }
        
        if (cur < 0)
            return i;
    }
    return enemy.size();
}