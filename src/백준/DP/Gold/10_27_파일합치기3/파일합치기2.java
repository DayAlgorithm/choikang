package 백준.Gold.파일합치기3;

import java.io.*;
import java.util.*;

public class 파일합치기2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            int k = Integer.parseInt(br.readLine());
            PriorityQueue<Long> pq = new PriorityQueue<>();
            StringTokenizer st = new StringTokenizer(br.readLine());

            for(int j=0;j<k;j++){
                pq.offer(Long.parseLong(st.nextToken()));
            }
            Long answer = solution(pq);
            sb.append(answer).append("\n");
        }
        System.out.print(sb);
    }

    public static Long solution(PriorityQueue<Long> pq) {
        Long answer = 0L;
        while(pq.size()>1){
            Long a = pq.poll();
            Long b = pq.poll();
            pq.offer(a+b);
            answer+=(a+b);
        }
        return answer;
    }
}
