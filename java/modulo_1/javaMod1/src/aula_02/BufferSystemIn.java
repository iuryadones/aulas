package aula_02;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BufferSystemIn {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		System.out.print("Escreva uma palavra e pressione o Enter: ");
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String read = br.readLine();
		
		System.out.println("Leitura do caracter: " + read);
	}
}
