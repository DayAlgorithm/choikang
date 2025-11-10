package 백준.Gold.행복유치원;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 행복유치원 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        // 키를 담을 배열
        int[] height = new int[n];
        st = new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++) {
             height[i] = Integer.parseInt(st.nextToken());
        }

        int[] gap = new int[n - 1];
        for (int i = 0; i < n-1; i++) {
            // 차이를 구하기 위해서 0부터 n-1까지 반복 왜? 순차대로 인덱스의 차를 gap에 넣어야 하는데
            // n까지 하면 인덱스 크기 초과 에러나서
            gap[i] = height[i + 1] - height[i];
        }

        // 5 3
        // 1 3 5 6 10
        // 2 2 1 4

        // k-1 만큼 즉 칸막이 수만큼 제일 갭이 큰걸 제거해주고 남은 값들의 합이 정답
        // 일단 내 풀이는 정렬해주고 k-1 만큼 빼주고 나머지 배열 값들의 합 구해주면 될듯
        Arrays.sort(gap);
        int result = 0;

        for (int i = 0; i < n-k; i++) { //전체 gap의 길이에서 k-1만큼(큰 값을 뺀 만큼) 더해서 결과 도출
            result += gap[i];
        }
        System.out.println(result);
    }
}
