/**
 * The ConcurrentExecution class demonstrates concurrent execution of two tasks using threads.
 */
public class ConcurrentExecution {

    public static void main(String[] args) {
        Thread task1Thread = new Thread(() -> {
            BackTrackingApproach.main(new String[]{}); // Run the non-recursive approach
        });

        Thread task2Thread = new Thread(() -> {
            RecursiveApproach.main(new String[]{}); // Run the recursive approach
        });

        task1Thread.start(); // Start the non-recursive approach
        task2Thread.start(); // Start the recursive approach

        try {
            task1Thread.join(); // Wait for the non-recursive approach to finish
            task2Thread.join(); // Wait for the recursive approach to finish
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
