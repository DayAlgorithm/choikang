package 백준.Gold.호텔;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 호텔 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int c = Integer.parseInt(st.nextToken()); // 인원수
        int n = Integer.parseInt(st.nextToken()); // 도시의 수

        // dp[] 배열 선언
        final int INF = 100_000_000;
        int[] dp = new int[c + 101];
        Arrays.fill(dp, INF);

        // 0명을 모으는데 0원이 든다(계산의 시작점)
        dp[0] = 0;

        for (int i = 0; i < n; i++) {
            // stringTokenizer는 매번 br.readline()을
            st = new StringTokenizer(br.readLine());
            int cost = Integer.parseInt(st.nextToken());
            int customer = Integer.parseInt(st.nextToken());

            for(int j=customer; j<=dp.length-1; j++) {
                dp[j] = Math.min(dp[j],dp[j-customer]+cost);
            }
        }
        int minCost = INF;
        for (int i = c; i < dp.length; i++) {
            minCost = Math.min(minCost, dp[i]);
        }
        System.out.println(minCost);
    }
}
