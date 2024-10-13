import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	String str1 =  br.readLine();
    	String str2 =  br.readLine();
    	int len1 = str1.length();
    	int len2 = str2.length();
    	// 테이블 만들기
    	
    	int[] tb = new int[len2];
    	int pidx = 0;
    	for(int i =1;i<len2;i++) {
    		// 접두 접미의 마지막 값이 각각 다르다면, 매칭되는 곳까지 탐색
    		while(pidx>0 && str2.charAt(pidx) != str2.charAt(i))
    			pidx = tb[pidx-1];

    		if(str2.charAt(i) == str2.charAt(pidx)) {
    			pidx += 1;
    			tb[i] = pidx;
    		}
    			
    	}
    	
    	// T
    	
    	StringBuilder sb = new StringBuilder();
    	int cnt = 0;
    	int i2 = 0;
    	
    	for(int i = 0; i < len1; i++) {
    		// 접
    		while(i2>0 && str1.charAt(i) != str2.charAt(i2))
    			i2 = tb[i2-1];
    		
    		if(i2<len2-1 && str1.charAt(i) == str2.charAt(i2)) {
    			i2++;
    		}
    		else if(i2 == len2-1 && str1.charAt(i) == str2.charAt(i2)) {
    			cnt++;
    			sb.append(i+1 - (len2-1)+" ");
    			i2 = tb[i2];
    		}
    	}
    	System.out.println(cnt);
    	System.out.println(sb);
    	
    }
    
}
