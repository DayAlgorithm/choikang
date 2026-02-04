package 백준.Silver.한_줄로_서기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 한줄로서기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n]; // 2 1 1 0

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] line = new int[n]; // 0 0 0 0

        for (int i = 0; i < n; i++) {
            int currentIndex = 0;
            int height = i+1; // 1
            int requiredIndex = arr[i]; //2
            for (int j = 0; j < n; j++) {
                // arr에 저장된 인덱스 수만큼 왼쪽이 비어져 있고 해당 값이 비어있으면 넣어준다
                if (currentIndex == requiredIndex && line[j] ==0) {
                    line[j] = height;
                    break;
                }
                if (line[j] == 0) {
                    currentIndex++;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(line[i]).append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}
