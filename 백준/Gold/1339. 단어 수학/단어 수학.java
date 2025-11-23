import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		int[] nums = new int[26];// A B C D E F G ...
		
		for(int i = 0 ;i< N;i++) {
			String str = br.readLine().trim();
			int len = str.length();
			for(int j = 0;j < len;j++) {
				
				nums[str.charAt(j) - 'A'] += Math.pow(10, len-1-j); 
			}
		}
		Arrays.sort(nums);
		int ans = 0;
		for(int i = 0 ;i<10;i++) {
			ans += i*nums[16 + i];
		}
		System.out.println(ans);
	}

}
