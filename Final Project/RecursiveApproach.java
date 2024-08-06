import java.util.HashSet;
import java.util.Set;

public class RecursiveApproach {
    private static int solutionCount = 0;

    /**
     * This method places queens on the board recursively. It places a queen in a
     * column and then moves to the next column. If it finds a safe position for the
     * queen, it places the queen and moves to the next column. If it doesn't find a
     * safe position, it backtracks and tries the next row in the previous column.
     * It keeps
     * track of the visited columns to check if the current position is symmetric to
     * any of the previously placed queens. If it is symmetric, it skips that
     * position.
     * 
     * @apiNote Time complexity analysis : In this approach, at each level branching
     *          factor
     *          decreases by 1 and it creates a new problem of size (n – 1) . With n
     *          choices,
     *          it creates n different problems of size (n – 1) at level 1.
     *          isSafe method determines if the current position being considered is
     *          safe,
     *          and runs in O(n) time. This method is called n times at each level,
     *          so the
     *          non-recurrence part of the complexity is O(n^2).
     *          Thus, the recurrence of 8-Queen problem is defined as, T(n) = n*T(n
     *          – 1) +
     *          n^2 where n is the size of the board, i.e. the number of queens to
     *          be placed,
     *          in this case 8. The solution to this recurrence is O(n!) where n is
     *          the size of
     *          the board.
     * 
     * @apiNote Space complexity analysis : The space complexity of the recursive
     *          approach is O(n) where n is the size of the board. The space
     *          complexity is
     *          determined by the space used by the visited set and the recursive
     *          stack.
     *          The visited set stores the columns that have already been visited,
     *          and the
     *          size of the set is at most n. The recursive stack stores the
     *          function calls
     *          and the maximum depth of the recursive stack is n (the number of
     *          queens to be
     *          placed). Thus, the space complexity of the recursive approach is
     *          O(n).
     * 
     * @param board   The board on which the queens are to be placed
     * @param x       The row in which the queen is to be placed
     * @param visited The set of columns that have already been visited
     */
    private static void placeQueens(Board board, int x, Set<Integer> visited) {
        int size = board.getSize();
        if (x == size) { // All queens have been placed (base case)
            // System.out.println();
            printQueens(board);
            // board.print();
            // System.out.println();
            solutionCount++;
            return;
        }

        for (int y = 0; y < size; y++) { // Try all columns in the current row x to place the queen (runs in O(n) time)

            if (board.isSafe(x, y)) { // Check if the current position is safe to place the queen (runs in O(n) time)
                board.setQueen(x, y); // Place the queen on the board (runs in O(1) time)
                visited.add(y); // Mark the column as visited (runs in O(1) time)
                placeQueens(board, x + 1, visited); // Move to the next row (recursive call) (runs until the base case
                                                    // is
                                                    // reached) (runs in O(n) time because it runs for as many queens
                                                    // that are supposed to be placed)
                visited.remove(y); // Backtrack and remove the y-coordinate from the set (runs in O(1) time)
                board.removeQueen(x); // Remove the queen from the board (runs in O(1) time)
            }
        }
    }

    private static void printQueens(Board board) {
        Queen[] queens = board.getQueens();
        for (int i = 0; i < queens.length; i++) {
            Queen queen = queens[i];
            if (queen != null) {
                System.out.print("(" + Integer.valueOf(queen.getX() + 1) + ", "
                        + Integer.valueOf(queen.getY() + 1) + ")");
                
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int size = 8;
        Board board = new Board(size);
        Set<Integer> visited = new HashSet<>();
        long startTime = System.currentTimeMillis();
        placeQueens(board, 0, visited);
        long endTime = System.currentTimeMillis();
        long executionTime = endTime - startTime;
        System.out.println("Number of solutions: " + solutionCount);
        System.out.println("Execution time: " + executionTime + " milliseconds");
    }
}