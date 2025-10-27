package 백준.Gold.파일합치기3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class 파일합치기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            int K = Integer.parseInt(br.readLine());
            PriorityQueue<Long> pq = new PriorityQueue<>();

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < K; i++) {
                pq.offer(Long.parseLong(st.nextToken()));
            }

            long result = solution(pq);
            sb.append(result).append('\n');
        }

        System.out.print(sb);
    }

    public static long solution(PriorityQueue<Long> pq) {
        long totalCost = 0;

        // 큐에 파일이 1개만 남을 때까지 반복
        while (pq.size() > 1) {
            // 가장 작은 두 파일을 꺼내서 합치기
            long first = pq.poll();
            long second = pq.poll();
            long sum = first + second;

            // 합친 비용을 총 비용에 누적
            totalCost += sum;

            // 합친 파일을 다시 큐에 넣기
            pq.offer(sum);
        }

        return totalCost;
    }
}
