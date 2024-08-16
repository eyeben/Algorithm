import java.io.*;
import java.util.*;

public class Solution {
    static LinkedList<Integer> arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        for(int tc = 1; tc<=10;tc++){
            arr = new LinkedList<>();
            br.readLine();
            st = new StringTokenizer(br.readLine());
            for(int i =0; i<8;i++){
                arr.addLast(Integer.parseInt(st.nextToken()));
            }
            int cnt = 0;
            while(true){
                int k = arr.pollFirst();
                cnt = 1 + cnt%5;
                k = Math.max(0, k-cnt);
                arr.addLast(k);
                if(k == 0)
                    break;
            }
            System.out.printf("#%d", tc);
            for(int itm: arr)
                System.out.printf(" %d",itm);
            System.out.println();

        }

    }
}