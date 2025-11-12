package 백준.Silver.한_줄로_서기;

import java.io.*;
import java.util.StringTokenizer;

public class 한줄로서기_11_01 {
    public static void main(String[] args) throws IOException {
        BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // n입력 받기
        int n = Integer.parseInt(br.readLine());
        // 입력 받은 값을 공백이나 빈칸을 기준으로 문자를 나눠주는 역할
        StringTokenizer st = new StringTokenizer(br.readLine());
        // n만큼의 공간을 할당
        int[] line = new int[n];
        // 토큰나이저에서 값을 하나씩 꺼내서 정수로 바꾼후 순서대로 배열에 삽입
        for (int i = 0; i < n; i++) {
            line[i] = Integer.parseInt(st.nextToken());
        }
        // 예를 들어 그럼 지금까지 n=4 line = [2,1,1,0]이 완성
        // 이 두 값을 매개변수로 받아서 출력을 반환하는 함수 생성
        int[] result = solution(n, line);
        for (int i = 0; i < result.length; i++) {
            sb.append(result[i]).append(" ");
        }
        // 여기가 조금 어색한거 같은데 도 좋은 방법 있는지 생각해보기
        System.out.println(sb.toString());
    }

    private static int[] solution(int n, int[] line) {
        //어차피 n과 line.length의 값이 같아서 n은 필요 없을거 같네
        // 정답을 담은 배열 선언 이건 초기화 되면 안되니까 for 밖에 선어
        int[] result = new int[n];

        for (int i = 0; i < line.length; i++) {
            // 처음 for문의 대상 첫번째는 그 사람의 키
            int height = i+1;
            // 현재 인덱스 위치 line에서 받은 값과 비교하기 위함
            // 이번에 깨달았는데 인덱스는 ++로 옮겨준다고 생각하면 됨
            int currentIndex = 0; //위에 두 값은 매번 위치가 옮겨짐에 따라 값이 초기화 되어야 하는것들

            for(int j=0;j<line.length;j++){
                // 자기보다 큰 사람의 수 즉 line[i]의 값과 비어있는 인덱스 수가 같고 최종배열에 값이 없다면
                if (line[i] == currentIndex && result[j] == 0) {
                    result[j] = height;
                    break;
                }

                if (result[j] == 0) {
                    currentIndex++;
                }
            }
        }
        return result;
    }
}
