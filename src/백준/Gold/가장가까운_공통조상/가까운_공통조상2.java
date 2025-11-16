package 백준.Gold.가장가까운_공통조상;

import java.io.*;
import java.util.*;

public class 가까운_공통조상2 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());

            // map을 이용해줘도 될거 같음 map을 이용해서 푸는 방법과 array를 이용해서 푸는 방법 2가지로 풀어보기
            int[] parents=new int[n + 1]; //n+1로 설정해준 이유는 인덱스를 1부터 사용하기 위함이고

            for (int i = 0; i < n - 1; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                parents[b]=a;
            }

            StringTokenizer st = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(st.nextToken());
            int node2 = Integer.parseInt(st.nextToken());

            int currentNode = node1;
            boolean[] visited = new boolean[n+1];
            while (currentNode != 0) {
                visited[currentNode] = true;
                currentNode = parents[currentNode];
            }

            currentNode = node2;
            while (currentNode != 0) {
                if (visited[currentNode]) {
                    System.out.println(sb.append(currentNode).toString());
                    break;
                }
                currentNode = parents[currentNode];
            }
        }

        //내가 헷갈렸던 부분 node1의 부모가 node2인데 그럼 node2는 부모 노드가 아리나 자신부터 검증해줘야 함
    }
}
