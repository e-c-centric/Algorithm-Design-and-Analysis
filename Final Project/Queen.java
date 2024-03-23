public class Queen {
    private int x, y;

    Queen(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public String toString() {
        return "(" + x + ", " + y + ")";
    }

    public boolean isAttacking(Queen otherQueen) {
        return x == otherQueen.getX() || y == otherQueen.getY()
                || Math.abs(x - otherQueen.getX()) == Math.abs(y - otherQueen.getY());
    }

    public boolean isAttacking(int x, int y) {
        return this.x == x || this.y == y || Math.abs(this.x - x) == Math.abs(this.y - y);
    }
}
