package 백준.Silver.수찾기;

import java.io.*;
import java.util.*;

public class 수찾기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int[] a = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(a);

        int m = Integer.parseInt(br.readLine());
        int[] b = new int[m];

        st = new StringTokenizer(br.readLine());
        for(int i=0;i<m;i++) {
            b[i] = Integer.parseInt(st.nextToken());
        }

        for(int i=0;i<m;i++) {
            if (binarySearch(a, b[i])) {
                sb.append("1").append('\n');
            } else {
                sb.append("0").append('\n');
            }
        }
        System.out.println(sb.toString().trim());
    }

    private static boolean binarySearch(int[] a, int m) {
        //1,2,3,4,5 5/2=2 a[2] =3
        int left=0;
        int right=a.length-1;

        while(left<=right) {
            int mid = (left + right) / 2; //중간값은 계속 바뀌어야 하니까 while루프 안으로 들어오는게 맞음
            if(m==a[mid]) {
                return true;
            } else if (m > a[mid]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return false;
    }
}
