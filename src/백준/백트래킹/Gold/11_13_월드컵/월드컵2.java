package 백준.Gold.월드컵;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class 월드컵2 {
    static ArrayList<int[]> matches = new ArrayList<>();
    static int[][] result = new int[6][3];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // 6경기에 나올 수 있는 모든 매치 15개의 경우를 리스트에 저장
        for (int i = 0; i < 6; i++) {
            for (int j = i + 1; j < 6; j++) {
                matches.add(new int[]{i, j});
            }
        }
        //System.out.println(Arrays.deepToString(matches.toArray()));

        // 6팀의 승무패의 정보를 받아 2차원 배열에 저장하기
        for (int t = 0; t < 4; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine()); //입력 받기
            boolean possible = true;

            for (int i = 0; i < 6; i++) {
                for (int j = 0; j < 3; j++) {
                    result[i][j] = Integer.parseInt(st.nextToken());
                }
                boolean istrue = true;
                if (result[i][0] + result[i][1] + result[i][2] != 5) {
                    possible=false;
                }
            }

            if (possible && dfs(0)) {
                sb.append("1 ");
            } else {
                sb.append("0 ");
            }
        }

        System.out.println(sb.toString().trim());
    }

    static boolean dfs(int matchIndex) {
        // 15번 경기를 치뤘는데 남아있는 승무패가 있다면 그 즉시 틀린 것이므로 false 반환하고 복귀
        if (matchIndex == 15) {
            for (int i = 0; i < 6; i++) {
                for(int j=0;j<3;j++){
                    if (result[i][j] != 0) {
                        return false;
                    }
                }
            }
            // 이 경우에 종료 조건
            return true;
        }

        // 위에 종료 조건이 아니라면 이어서 진행
        // team은 재귀 들어가면 matchIndex가 1씩 커짐 그래서 이건 따로 선언해줘야 하는거
        int teamA = matches.get(matchIndex)[0];
        int teamB = matches.get(matchIndex)[1];

        if (result[teamA][0] > 0 && result[teamB][2] > 0) {
            result[teamA][0]--;
            result[teamB][2]--;
            if(dfs(matchIndex+1)) return true;
            result[teamA][0]++;
            result[teamB][2]++;
        }

        if(result[teamA][1]>0 && result[teamB][1]>0){
            result[teamA][1]--;
            result[teamB][1]--;
            if(dfs(matchIndex+1)) return true;
            result[teamA][1]++;
            result[teamB][1]++;
        }

        if (result[teamA][2] > 0 && result[teamB][0] > 0) {
            result[teamA][2]--;
            result[teamB][0]--;
            if(dfs(matchIndex+1)) return true;
            result[teamA][2]++;
            result[teamB][0]++;
        }

        return false;

    }
}
