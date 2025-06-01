import java.util.Scanner;

class Codechef
{
	public static void main (String[] args) 
	{
		// your code goes here
		Scanner sc = new Scanner(System.in);
		int num1 = sc.nextInt();
		int num2 = sc.nextInt();
		int[] numbers = new int[num1];
		int[] numbers2 = new int[num2];
		
		for (int i = 0; i<num1; i++){
		    numbers[i] = sc.nextInt();
		}
		for (int i = 0; i<num2; i++){
		    numbers2[i] = sc.nextInt();
		}
		
		for (int i = 0; i<num1; i++){
		    System.out.print(numbers[i]+" ");
		}
		for (int i = 0; i<num2; i++){
		    System.out.print(numbers2[i]+" ");
		}
		for (int i = 0; i<num1; i++){
		    System.out.print(numbers[i]+" ");
		}

	}
}
