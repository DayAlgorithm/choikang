package 빅데이터.공유카운터;

import java.util.EmptyStackException;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class SpinLock<T> {
    private Lock lock;
    private int head;
    private int tail;
    private T[] items;

    public SpinLock(int cap) {
        lock = new ReentrantLock();
        items = (T[]) new Object[cap];
        head = 0;
        tail = 0;
    }

    public T deq() {
        lock.lock();
        try {
            if (head == tail) {
                throw new EmptyStackException();
            }
            T x = items[head % items.length];
            items[head % items.length] = null;
            head++;
            return x;
        }finally {
            lock.unlock();
        }
    }
}

