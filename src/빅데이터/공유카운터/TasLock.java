package 빅데이터.공유카운터;


import java.util.concurrent.atomic.AtomicBoolean;

// 1. 하드웨어의 TAS 동작을 흉내 낸 클래스 (개념 이해용)
class MyAtomicBoolean {
    private boolean value;

    public MyAtomicBoolean(boolean initialValue) {
        this.value = initialValue;
    }

    // 여기가 핵심! (사용자님이 주신 코드)
    // 하드웨어에서는 이 과정이 '원자적(Atomic)'으로 한 번에 일어납니다.
    public synchronized boolean getAndSet(boolean newValue) {
        boolean prior = value; // 1. 이전 값을 기억한다 (Old Value)
        value = newValue;      // 2. 무조건 새 값으로 덮어쓴다 (Write)
        return prior;          // 3. 기억해둔 이전 값을 반환한다
    }

    public synchronized void set(boolean newValue) {
        this.value = newValue;
    }
}

// 2. 위 클래스를 이용한 TAS 락 구현
public class TasLock {
    // 락의 상태 (false: 풀림, true: 잠김)
    AtomicBoolean state = new AtomicBoolean(false);

    public void lock() {
        // -------------------------------------------------------
        // [핵심 로직]
        // 1. state.getAndSet(true)를 실행한다.
        // 2. 만약 반환값이 false라면? (내가 1등으로 잠금) -> 루프 탈출, 락 획득!
        // 3. 만약 반환값이 true라면? (누가 이미 잠가둠) -> 계속 뺑뺑이 (Spin)
        // -------------------------------------------------------
        while (state.getAndSet(true)) {
            // 락을 얻을 때까지 무한 대기 (Busy Wait)
        }
    }

    public void unlock() {
        // 락을 푼다 (상태를 false로 변경)
        state.set(false);
    }
}
