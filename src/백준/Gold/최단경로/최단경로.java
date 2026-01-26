package 백준.Gold.최단경로;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

// 1. 도착 지점과 가중치를 담을 Node 클래스 (Comparable 구현)
class Node implements Comparable<Node> {
    int end;
    int weight;

    public Node(int end, int weight) {
        this.end = end;
        this.weight = weight;
    }

    // 우선순위 큐에서 가중치가 작은 순서대로 정렬되도록 설정
    @Override
    public int compareTo(Node other) {
        return this.weight - other.weight;
    }
}

public class 최단경로 {
    // 무한대를 의미하는 값 (가중치 최대 10 * 정점 최대 20,000 = 200,000 이므로 넉넉하게 설정)
    static final int INF = 100_000_000;
    static int v, e, k;
    static ArrayList<Node>[] graph; // 인접 리스트
    static int[] dist; // 최단 거리 테이블

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        v = Integer.parseInt(st.nextToken()); // 정점의 개수
        e = Integer.parseInt(st.nextToken()); // 간선의 개수
        k = Integer.parseInt(br.readLine()); // 시작 정점 번호

        // 2. 그래프 초기화 (ArrayList의 배열 사용)
        graph = new ArrayList[v + 1];
        for (int i = 1; i <= v; i++) {
            graph[i] = new ArrayList<>();
        }

        // 최단 거리 테이블 초기화 (모두 INF로)
        dist = new int[v + 1];
        Arrays.fill(dist, INF);

        // 3. 간선 정보 입력 받기
        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            // start에서 end로 가는 가중치 weight인 간선 추가
            graph[start].add(new Node(end, weight));
        }

        // 4. 다익스트라 알고리즘 실행
        dijkstra(k);

        // 5. 결과 출력
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= v; i++) {
            if (dist[i] == INF) {
                sb.append("INF\n");
            } else {
                sb.append(dist[i]).append("\n");
            }
        }
        System.out.print(sb);
    }

    // 다익스트라 알고리즘
    private static void dijkstra(int start) {
        // 우선순위 큐 생성 (가중치 오름차순)
        PriorityQueue<Node> pq = new PriorityQueue<>();

        // 시작점 초기화
        pq.add(new Node(start, 0));
        dist[start] = 0;

        while (!pq.isEmpty()) {
            // 큐에서 가장 거리가 짧은 노드 꺼내기
            Node currentNode = pq.poll();
            int curIdx = currentNode.end;
            int curDist = currentNode.weight;

            // [방문 처리] 현재 꺼낸 거리보다 이미 저장된 거리가 더 짧다면 스킵 (이미 방문한 셈)
            if (dist[curIdx] < curDist) {
                continue;
            }

            // 현재 노드와 연결된 주변 노드들 확인
            for (Node nextNode : graph[curIdx]) {
                // (현재까지 온 거리 + 다음 노드로 가는 거리) 계산
                int cost = dist[curIdx] + nextNode.weight;

                // 계산한 거리가 기존에 알고 있던 거리보다 짧다면 갱신
                if (cost < dist[nextNode.end]) {
                    dist[nextNode.end] = cost;
                    // 갱신된 정보를 큐에 넣기
                    pq.add(new Node(nextNode.end, cost));
                }
            }
        }
    }
}