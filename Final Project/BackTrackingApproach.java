// Comparison of backtracking(non-recursive) and recursive versions of the
// algorithms for solving the 8 Queen Problem

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class BackTrackingApproach {
    public static List<int[][]> uniqueSolutions = new ArrayList<>();

    public static void solve(Board board) {
        List<int[][]> solutions = new ArrayList<>();
        int size = board.getSize();
        Stack<int[]> queensPositions = new Stack<>();
        int j = 0;
        for (int i = 0; i < size;) {
            for (; j < size; j++) {
                if (board.isSafe(i, j)) {
                    board.setQueen(i, j);
                    queensPositions.push(new int[] { i, j });
                    break;
                }
            }
            if (queensPositions.size() != i + 1) {
                if (!queensPositions.empty()) {
                    int[] lastQueen = queensPositions.pop();
                    board.removeQueen(lastQueen[0]);
                    i = lastQueen[0];
                    j = lastQueen[1] + 1;
                    continue;
                }
            } else {
                j = 0;
            }
            if (i == size - 1) {
                solutions.add(queensPositions.stream().map(int[]::clone).toArray(int[][]::new));
                if (!queensPositions.empty()) {
                    int[] lastQueen = queensPositions.pop();
                    board.removeQueen(lastQueen[0]);
                    i = lastQueen[0];
                    j = lastQueen[1] + 1;
                    continue;
                }
            }
            i++;
        }

        for (int[][] solution : solutions) {
            boolean isUnique = true;
            for (int[][] uniqueSolution : uniqueSolutions) {
                boolean isEqual = true;
                for (int i = 0; i < solution.length; i++) {
                    if (solution[i][0] != uniqueSolution[i][0] || solution[i][1] != uniqueSolution[i][1]) {
                        isEqual = false;
                        break;
                    }
                }
                if (isEqual) {
                    isUnique = false;
                    break;
                }
            }
            if (isUnique) {
                uniqueSolutions.add(solution);
            }
        }
    }

    static List<int[][]> validateSolutions(List<int[][]> solutions) {
        List<int[][]> validSolutions = new ArrayList<>();
        for (int[][] solution : solutions) {
            boolean isValid = true;
            for (int i = 0; i < solution.length; i++) {
                for (int j = i + 1; j < solution.length; j++) {
                    if (solution[i][0] == solution[j][0] || solution[i][1] == solution[j][1]
                            || Math.abs(solution[i][0] - solution[j][0]) == Math.abs(solution[i][1] - solution[j][1])) {
                        isValid = false;
                        break;
                    }
                }
                if (!isValid) {
                    break;
                }
            }
            if (isValid) {
                validSolutions.add(solution);
            }
        }
        return validSolutions;
    }

    public static void main(String[] args) {
        Board board = new Board(8);
        solve(board);
        if (!uniqueSolutions.isEmpty()) {
            for (int[][] solution : uniqueSolutions) {
                for (int[] position : solution) {
                    System.out.print("(" + (position[0] + 1) + ", " + (position[1] + 1) + ") ");
                }
                System.out.println();
            }
        } else {
            System.out.println("No solution found");
        }

        System.out.println("Number of solutions: " + uniqueSolutions.size());

        List<int[][]> validSolutions = validateSolutions(uniqueSolutions);
        if (!validSolutions.isEmpty()) {
            for (int[][] solution : validSolutions) {
                for (int[] position : solution) {
                    System.out.print("(" + (position[0] + 1) + ", " + (position[1] + 1) + ") ");
                }
                System.out.println();
            }
        } else {
            System.out.println("No valid solution found");
        }

        System.out.println("Number of valid solutions: " + validSolutions.size());
    }

}