<<<<<<< HEAD
/**
 * The Queen class represents a queen on a chessboard.
 * It stores the position of the queen on the chessboard and provides methods to access and manipulate the position.
 */
public class Queen {
    private int x, y;

    /**
     * Constructs a Queen object with the specified position.
     *
     * @param x the x-coordinate of the queen's position
     * @param y the y-coordinate of the queen's position
     */
    Queen(int x, int y) {
        this.x = x;
        this.y = y;
    }

    /**
     * Returns the x-coordinate of the queen's position.
     *
     * @return the x-coordinate of the queen's position
     */
    public int getX() {
        return x;
    }

    /**
     * Returns the y-coordinate of the queen's position.
     *
     * @return the y-coordinate of the queen's position
     */
    public int getY() {
        return y;
    }

    /**
     * Returns a string representation of the queen's position.
     *
     * @return a string representation of the queen's position
     */
    public String toString() {
        return "(" + x + ", " + y + ")";
    }

    /**
     * Checks if this queen is attacking another queen.
     *
     * @param otherQueen the other queen to check against
     * @return true if this queen is attacking the other queen, false otherwise
     */
    public boolean isAttacking(Queen otherQueen) {
        return x == otherQueen.getX() || y == otherQueen.getY()
                || Math.abs(x - otherQueen.getX()) == Math.abs(y - otherQueen.getY());
    }

    /**
     * Checks if this queen is attacking a position on the chessboard.
     *
     * @param x the x-coordinate of the position to check
     * @param y the y-coordinate of the position to check
     * @return true if this queen is attacking the position, false otherwise
     */
    public boolean isAttacking(int x, int y) {
        return this.x == x || this.y == y || Math.abs(this.x - x) == Math.abs(this.y - y);
    }
}
=======
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
>>>>>>> 9681e1f43439df2f2b411d2e26963757fec5caae
