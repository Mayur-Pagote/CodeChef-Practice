import java.util.*;
import java.lang.*;
import java.io.*;
class Codechef {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        if (n > 5) {            
            System.out.println("the number is greater than 5");
        } else {
            System.out.println("the number is smaller than or equal to 5");
        }
        
        scanner.close();
    }
}
