import java.util.List;

/**
 * The Board class represents a chess board for the N-Queens problem.
 * It provides methods for setting and removing queens on the board,
 * checking if a position is safe for a queen, and printing the board.
 */
public class Board {
    private Queen[] queens;
    private int size;

    /**
     * Constructs a Board object with the specified size.
     *
     * @param size the size of the board
     */
    Board(int size) {
        this.size = size;
        queens = new Queen[size];
    }

    /**
     * Sets a queen at the specified position on the board.
     *
     * @param x the x-coordinate of the position
     * @param y the y-coordinate of the position
     */
    public void setQueen(int x, int y) {
        queens[x] = new Queen(x, y);
    }

    /**
     * Removes the queen at the specified position on the board.
     *
     * @param x the x-coordinate of the position
     */
    public void removeQueen(int x) {
        queens[x] = null;
    }

    /**
     * Checks if the specified position is safe for a queen.
     * A position is safe if no other queen can attack it.
     *
     * @param x the x-coordinate of the position
     * @param y the y-coordinate of the position
     * @return true if the position is safe, false otherwise
     */
    public boolean isSafe(int x, int y) {
        for (int i = 0; i < size; i++) {
            if (queens[i] != null && queens[i].isAttacking(new Queen(x, y))) {
                return false;
            }
        }
        return true;
    }

    /**
     * Prints the current state of the board.
     * Queens are represented by 'Q' and empty cells are represented by '-'.
     */
    public void print() {
        char[][] grid = new char[size][size];
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                grid[i][j] = '-';
            }
        }
        for (int i = 0; i < size; i++) {
            if (queens[i] != null) {
                int x = queens[i].getX();
                int y = queens[i].getY();
                grid[x][y] = 'Q';
            }
        }
        for (int i = 0; i < size; i++) {
            System.out.print("+");
            for (int j = 0; j < size; j++) {
                System.out.print("---+");
            }
            System.out.println();
            for (int j = 0; j < size; j++) {
                System.out.print("| " + grid[i][j] + " ");
            }
            System.out.println("|");
        }
        System.out.print("+");
        for (int j = 0; j < size; j++) {
            System.out.print("---+");
        }
        System.out.println();
    }

    /**
     * Prints the board with the specified solution.
     *
     * @param solution the solution to be printed
     */
    public void print(int[][] solution) {
        char[][] grid = new char[size][size];
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                grid[i][j] = '-';
            }
        }
        for (int i = 0; i < size; i++) {
            int x = solution[i][0];
            int y = solution[i][1];
            grid[x][y] = 'Q';
        }
    }

    /**
     * Prints the board for each solution in the specified list of solutions.
     *
     * @param solutions the list of solutions to be printed
     */
    public void print(List<int[][]> solutions) {
        for (int[][] solution : solutions) {
            if (solution.length == 0) {
                continue;
            }
            char[][] grid = new char[size][size];
            for (int i = 0; i < size; i++) {
                for (int j = 0; j < size; j++) {
                    grid[i][j] = '-';
                }
            }
            for (int i = 0; i < size; i++) {
                int x = solution[i][0];
                int y = solution[i][1];
                grid[x][y] = 'Q';
            }
            System.out.println();
            for (int i = 0; i < size; i++) {
                System.out.print("+");
                for (int j = 0; j < size; j++) {
                    System.out.print("---+");
                }
                System.out.println();
                for (int j = 0; j < size; j++) {
                    System.out.print("| " + grid[i][j] + " ");
                }
                System.out.println("|");
            }
            System.out.print("+");
            for (int j = 0; j < size; j++) {
                System.out.print("---+");
            }
            System.out.println();

        }
    }

    /**
     * Returns the size of the board.
     *
     * @return the size of the board
     */
    public int getSize() {
        return size;
    }

    /**
     * Returns the array of queens on the board.
     *
     * @return the array of queens
     */
    Queen[] getQueens() {
        return queens;
    }

    
}
