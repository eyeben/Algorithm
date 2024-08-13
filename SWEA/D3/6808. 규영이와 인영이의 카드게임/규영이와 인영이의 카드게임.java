import java.io.*;
import java.util.*;
 
public class Solution {
    static List<Integer> cards1 = new ArrayList<>();
    static List<Integer> cards2 = new ArrayList<>();
    static int winCnt = 0;
    static int loseCnt = 0; 
 
    public static void main(String[] args) throws NumberFormatException, IOException {
         
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
         
        for(int t = 1;t<=N;t++) {
        	// 케이스 별 초기화
            winCnt = 0;
            loseCnt = 0;
            cards1 = new ArrayList<>();
            cards2 = new ArrayList<>();
            
            // 입력받은 숫자를 cards1에 저장하고 nums에 마킹
            st = new StringTokenizer(br.readLine());
            boolean[] nums = new boolean[19];
            for(int i =0; i<9;i++) {
                cards1.add(Integer.parseInt(st.nextToken()));
                nums[cards1.get(i)] = true;
            }
            
            // 마킹 안된 숫자들을 card2에 저장
	        for(int i =1; i<19;i++)
	            if(!nums[i])
	                cards2.add(i);

	        // 게임 수행 후 출력
	        permutation(0);
	        System.out.printf("#%d %d %d\n", t, winCnt, loseCnt);
	         
        }
         
         
    }

    // card2 순열을 생성하고 점수를 더함
    static void permutation(int depth) {
        if (depth == 9) {
            addScore();
            return;
        }
        // 재귀함수를 이용하여 List의 앞에서 뒤까지 모든 경우의 수를 채워간다
        for(int i = depth; i<9;i++) {
            swap(depth,i);
            permutation(depth+1);
            swap(depth,i);
        }
         
    }
    
     // 인덱스 두개를 기준으로 card2의 요소를 서로 교환
    static void swap(int idx1, int idx2) {
        int tmp = cards2.get(idx1);
        cards2.set(idx1, cards2.get(idx2));
        cards2.set(idx2, tmp);
    }   
    
    // 현재 card1, card2 상태를 기준으로 점수 추가
    static void addScore() {
        int cnt1 = 0, cnt2 = 0, ans = 0;
         
        for(int i = 0;i < 9;i++) {
            if(cards1.get(i) < cards2.get(i))
                cnt2+= cards1.get(i) + cards2.get(i);
            else
                cnt1+= cards1.get(i) + cards2.get(i);
        }
        
        ans = cnt2-cnt1;
        if(ans < 0)
            winCnt++;
        else if(ans > 0)
            loseCnt++;
         
    }
 
}