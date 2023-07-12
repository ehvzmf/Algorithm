package cote;
import java.util.Scanner;
import java.util.Arrays;

public class ATM {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		
		int N = in.nextInt();
		int[] arr = new int[N];
		for(int i = 0; i < N; i++) {
			arr[i] = in.nextInt();
		}
		
		//sort
		Arrays.sort(arr);
		
		int prev = 0;
		int sum = 0;
		
		for(int i = 0; i < N; i++) {
			sum += prev + arr[i];
			prev += arr[i];
		}
		System.out.println(sum);

	}

}
