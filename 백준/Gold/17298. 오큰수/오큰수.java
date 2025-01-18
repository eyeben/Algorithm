import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int [] arr = new int[N];
        for (int i = 0; i < N; i++)
            arr[i] = sc.nextInt();

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(o -> o[0]));

        pq.add(new int[]{arr[0], 0});
        int[] ans = new int[N];
        Arrays.fill(ans, -1);

        for(int i = 1; i < N; i++){
            int num = arr[i];
            while (!pq.isEmpty() && pq.peek()[0] < num){
                int[] temp = pq.poll();
                ans[temp[1]] = num;
            }
            pq.add(new int[]{arr[i], i});
        }

        StringBuilder sb = new StringBuilder();
        for(int itm:ans){
            sb.append(itm).append(" ");
        }
        System.out.println(sb);


    }
}