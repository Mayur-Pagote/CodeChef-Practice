// Debug the code below to solve the problem.
import java.util.Scanner;

class Codechef
{
	public static void main (String[] args) 
	{
		Scanner scanner = new Scanner(System.in);

        int i = 1, N, sum = 0;
        N = scanner.nextInt();

        while (i <= N) {
            sum += i;
            i++;
        }
        System.out.println(sum);
	}
}
