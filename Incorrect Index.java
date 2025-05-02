import java.util.*;

class Codechef{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.next(); // Input string
        scanner.close();

        if (s.length() >= 6) {
            
            char c1 = s.charAt(0); 
            char c2 = s.charAt(3);
            char c3 = s.charAt(5);

            System.out.println("" + c1 + c2 + c3);
        } else {
            // Handle the case when indices are out of bounds
            System.out.println("Invalid indices"); 
        }
    }
}
