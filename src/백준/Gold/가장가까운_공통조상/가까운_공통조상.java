package 백준.Gold.가장가까운_공통조상;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 가까운_공통조상 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine()); //테스트 케이스 수

        // t가 2이면 2번 실행 t-- 이기 때문에 2 그리고 1 실행되고 0일때는 실행 x
        while (t-->0) {
            // 정점 n을 받기
            int n = Integer.parseInt(br.readLine());
            // 부모 배열 선언
            int[] parent = new int[n + 1];
            // 부모 자식 관계 맺어주기
            for(int i=0;i<n-1;i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken()); //부모
                int b = Integer.parseInt(st.nextToken()); //자식
                // 부모 자식 연결
                parent[b] = a; // b의 부모는 a이다
            }

            // 조상을 구할 노드 2개
            StringTokenizer st = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(st.nextToken());
            int node2 = Integer.parseInt(st.nextToken());

            // 가까운 조상 찾아주기
            // 조상을 타고 올라가면서 방문 체크 해줄 배열 선언
            boolean[] visited = new boolean[n + 1];
            // 조상을 타고 올라갈걸 어떻게 구현할거야 강아
            // 올라가야 하니까 부모 정보를 저장할 parent 배열이 필요하겠구나
            int currentNode = node1;
            while (currentNode != 0) {
                visited[currentNode] = true;
                currentNode=parent[currentNode];
            }

            currentNode = node2;
            // 현재 노드가 parent[c  urrentNode]가 0이 아니다
            while(currentNode!=0){
                if(visited[currentNode]){
                    System.out.println(currentNode);
                    break;
                }
                currentNode = parent[currentNode];
            }
        }
    }
}
