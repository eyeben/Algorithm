#include <iostream>
#include <deque>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

    int N, L;
    deque<pair<int, int>> dq;
    cin >> N >> L;

    for (int i = 0; i < N; i++){
        int tmp;
        cin >> tmp;

        while (dq.size() && dq.back().second > tmp)
            dq.pop_back();

        dq.push_back(make_pair(i, tmp));
        if(dq.front().first == i - L)
            dq.pop_front();
        cout << dq.front().second << ' ';

                
            
    }

}