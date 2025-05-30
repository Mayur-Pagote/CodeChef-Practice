import java.util.Scanner;

class Codechef
{
	public static void main (String[] args) 
	{
		// your code goes here
		
		Scanner scanner = new Scanner(System.in);
		int size = scanner.nextInt();
		int[] numbers = new int[size+2];
		numbers[0] = 0;
		for (int i = 1; i<=size; i++){
		    int user = scanner.nextInt();
		    numbers[i] = user;
		}
		
		int newint = scanner.nextInt();
		numbers[0] = newint;
		numbers[size+1] = newint;
		
		for (int j = 0; j<size+2; j++){
		    System.out.print(numbers[j]+" ");
		}


	}
}
