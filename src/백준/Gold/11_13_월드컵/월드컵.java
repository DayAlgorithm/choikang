package 백준.Gold.월드컵;

import java.io.*;
import java.util.StringTokenizer;

public class 월드컵 {
    static int[][] result;
    static int[][] matches;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // 6개 팀의 모든 경기 조합 생성 (15경기)
        matches = new int[15][2];
        int idx = 0;
        for (int i = 0; i < 6; i++) {
            for (int j = i + 1; j < 6; j++) {
                matches[idx][0] = i;
                matches[idx][1] = j;
                idx++;
            }
        }

        // 4개의 테스트 케이스 처리
        for (int t = 0; t < 4; t++) {
            result = new int[6][3]; // 6개 팀, [승, 무, 패]
            StringTokenizer st = new StringTokenizer(br.readLine());

            boolean possible = true;
            for (int i = 0; i < 6; i++) {
                for (int j = 0; j < 3; j++) {
                    result[i][j] = Integer.parseInt(st.nextToken());
                }
                // 각 팀은 5경기를 해야 함
                if (result[i][0] + result[i][1] + result[i][2] != 5) {
                    possible = false;
                }
            }

            if (possible && dfs(0)) {
                sb.append("1 ");
            } else {
                sb.append("0 ");
            }
        }

        System.out.println(sb);
    }

    static boolean dfs(int matchIdx) {
        // 15경기를 모두 처리했으면
        if (matchIdx == 15) {
            // 모든 팀의 승무패가 0인지 확인
            for (int i = 0; i < 6; i++) {
                for (int j = 0; j < 3; j++) {
                    if (result[i][j] != 0) {
                        return false;
                    }
                }
            }
            return true;
        }

        int teamA = matches[matchIdx][0];
        int teamB = matches[matchIdx][1];

        // 경우 1: A팀 승, B팀 패
        if (result[teamA][0] > 0 && result[teamB][2] > 0) {
            result[teamA][0]--;
            result[teamB][2]--;
            if (dfs(matchIdx + 1)) return true;
            result[teamA][0]++;
            result[teamB][2]++;
        }

        // 경우 2: 무승부
        if (result[teamA][1] > 0 && result[teamB][1] > 0) {
            result[teamA][1]--;
            result[teamB][1]--;
            if (dfs(matchIdx + 1)) return true;
            result[teamA][1]++;
            result[teamB][1]++;
        }

        // 경우 3: A팀 패, B팀 승
        if (result[teamA][2] > 0 && result[teamB][0] > 0) {
            result[teamA][2]--;
            result[teamB][0]--;
            if (dfs(matchIdx + 1)) return true;
            result[teamA][2]++;
            result[teamB][0]++;
        }

        return false;
    }
}
