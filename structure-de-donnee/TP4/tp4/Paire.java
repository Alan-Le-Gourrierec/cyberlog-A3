package tp4;

public class Paire<A,B> {
    private final A first;
    private final B second;

    public Paire(A first, B second) {
        this.first = first;
        this.second = second;
    }
    
    public A getFirst() {
        return first;
    }
    
    public B getSecond() {
        return second;
    }
}