package aula_03;

import java.util.Scanner;

public class ToEqualBoolean_0 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		System.out.print("Variável b1: ");
		int b1 = scan.nextInt();
		
		System.out.print("Variável b2: ");
		int b2 = scan.nextInt();
		
		boolean resp;
		
		resp = b1 == b2;
		
		
		System.out.println("\nResposta: " + resp);
	}

}
