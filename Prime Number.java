import java.util.Scanner;

class Codechef
{
	public static void main (String[] args) 
	{
		Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        boolean isPrime = true; // Assum n is prime.

        for (int i=2; i<=n/2; i++){
            if (n%i == 0) isPrime = false;
        }
        
        if (isPrime) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
	}
}
