import java.util.Scanner;
class Codechef
{
	public static void main (String[] args) 
	{
		int[] array = new int[100]; // Initial array
		array[0] = 2;
	    array[1] = 4;
	    array[2] = 6;
	    array[3] = 8;
	    array[4] = 10;
        int size = 5; // Current size of the array

        int positionToDelete = 2; // Index of the element to delete

        // Update the code to shift elements to fill the gap left by the deleted element
        
        for (int i = positionToDelete; i<size-1; i++){
            array[i] = array[i+1];
        }
        
        size--;
    

        // Print the updated array
        for (int i = 0; i < size; i++) {
            System.out.print(array[i] + " ");
        }
	}
}
