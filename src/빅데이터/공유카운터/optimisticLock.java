package 빅데이터.공유카운터;

public class optimisticLock<T> {
    public boolean remove(T item) {
        int key = item.hashCode();
        retry:
        while (true) {
            Node pred = head;
            Node curr = pred.next;
            while (curr.key <= key) {
                if(curr)
            }
        }
    }

    public void a() {
        int value;

        public boolean sychronized cas(int expect, int update){
            if (value == expect) {
                value=update;
                return true;
            }
            return false;
        }
    }



    boolean validate(Node prec, Node curr) {
        Node node = head;
        while (node.key <= prec.key) {
            if (node == prec) {
                return prec.key == curr;
            }
        }
        return false;
    }
}
