package 프로그래머스.Level1.조이스틱;

public class 조이스틱 {
    public int solution(String name) {
        int answer=0;
        int length = name.length();
        int move = length-1;
        for(int i=0; i<length; i++){
            char c = name.charAt(i);
            answer += Math.min(c-'A', 'Z'-c+1); // 26-24+1 z-x

            //name에서 for문을 도는 동안 다음 c가 a인지 확인
            int next = i+1;
            while (next < length && name.charAt(next) == 'A') {
                next++;
            }

            move = Math.min(move, i * 2 + length - next);
            move = Math.min(move, (length-next)*2 + i);
        }
        answer += move;
        return answer;
    }
}
