import java.util.Scanner;

class Codechef
{
	public static void main (String[] args) 
	{
		Scanner scanner = new Scanner(System.in);
        int num, count = 0;
        num = scanner.nextInt();

        while (num != 0) {
            // Update your code below this line.
            count += 1;
            num = num/10;
            
        }
        System.out.println(count);
	}
}
