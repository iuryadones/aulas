package aula_02;

import java.util.Scanner;

public class ScannerSystemIn {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.print("Digite um número: ");
		
		Scanner scan = new Scanner(System.in);
		
		int b1 = scan.nextInt();
		
		System.out.println("numero: " + b1);
	}

}
