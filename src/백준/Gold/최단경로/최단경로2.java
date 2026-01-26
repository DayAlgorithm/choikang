package 백준.Gold.최단경로;

import java.io.*;
import java.util.*;

record Node2(int end, int weight) {}

public class 최단경로2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(br.readLine());

        // 2. 그래프 초기화 (여전히 반복문은 필요합니다)
        ArrayList<Node2>[] graph = new ArrayList[V + 1];
        for (int i = 1; i <= V; i++) graph[i] = new ArrayList<>();

        // 3. 간선 입력
        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph[u].add(new Node2(v, w));
        }

        // 4. 다익스트라 준비
        int[] dist = new int[V + 1];
        Arrays.fill(dist, 100_000_000); // INF값 직접 입력 (상수 선언 생략)
        dist[K] = 0;

        // 5. 우선순위 큐 (람다식으로 정렬 기준 정의: 가중치 기준 오름차순)
        PriorityQueue<Node2> pq = new PriorityQueue<>((a, b) -> a.weight() - b.weight());
        pq.add(new Node2(K, 0));

        // 6. 다익스트라 로직
        while (!pq.isEmpty()) {
            Node2 cur = pq.poll();

            // 방문 처리 (레코드 필드는 .end(), .weight()로 접근하거나 변수명 그대로 접근)
            if (dist[cur.end()] < cur.weight()) continue;

            for (Node2 next : graph[cur.end()]) {
                int nextDist = dist[cur.end()] + next.weight();
                if (nextDist < dist[next.end()]) {
                    dist[next.end()] = nextDist;
                    pq.add(new Node2(next.end(), nextDist));
                }
            }
        }

        // 7. 출력
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= V; i++) {
            sb.append(dist[i] == 100_000_000 ? "INF" : dist[i]).append('\n');
        }
        System.out.print(sb);
    }
}
