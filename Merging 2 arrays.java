import java.util.Scanner;

class Codechef
{
	public static void main (String[] args) 
	{
		int firstArray[] = new int[100]; // First array
        firstArray[0] = 2;
        firstArray[1] = 4;
        firstArray[2] = 6;
        int size1 = 3;

        int secondArray[] = new int[100]; // Second array
        secondArray[0] = 8;
        secondArray[1] = 10;
        secondArray[2] = 12;
        secondArray[3] = 14;
        int size2 = 4;
        
        // Update the code below to solve the problem.

        int mergedSize = size1+size2;
        int mergedArray[] = new int[mergedSize];
        for (int i = 0; i<size1; i++){
            mergedArray[i] = firstArray[i];
        }
        for (int j = 0; j<size2; j++){
            mergedArray[j+3] = secondArray[j];
        }




        // Print the merged array
        for (int i = 0; i < mergedSize; i++) {
            System.out.print(mergedArray[i] + " ");
        }

	}
}
