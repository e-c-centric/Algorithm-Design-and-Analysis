public class Board {
    private Queen[] queens;
    private int size;

    Board(int size) {
        this.size = size;
        queens = new Queen[size];
    }

    public void setQueen(int x, int y) {
        queens[x] = new Queen(x, y);
    }

    public void removeQueen(int x) {
        queens[x] = null;
    }

    public boolean isSafe(int x, int y) {
        for (int i = 0; i < size; i++) {
            if (queens[i] != null && queens[i].isAttacking(new Queen(x, y))) {
                return false;
            }
        }
        return true;
    }

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

    public int getSize() {
        return size;
    }

    Queen[] getQueens() {
        return queens;
    }

    public static void main(String[] args) {
        Board board = new Board(8);
        board.setQueen(0, 0);
        board.setQueen(1, 4);
        board.setQueen(2, 7);
        board.setQueen(3, 5);
        board.setQueen(4, 2);
        board.setQueen(5, 6);
        board.setQueen(6, 1);
        board.setQueen(7, 3);
        board.print();
    }

}
