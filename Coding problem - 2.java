import java.util.Scanner;

class Codechef
{
	public static void main (String[] args) 
	{
		
		Scanner sc = new Scanner(System.in);
		int user = sc.nextInt();
		int[] numbers = new int[user];
		
		for (int i = 0; i<user; i++){
		    numbers[i] = sc.nextInt();
		}
		
		int num = sc.nextInt();
		
		for (int j = 0; j<user; j++){
		    if (numbers[j] != num) System.out.print(numbers[j]+" ");
		}
		
		

	}
}
