package aula_02;

import java.io.IOException;

public class SystemInRead {


	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		System.out.print("Tecle uma vez e pressione o Enter: ");
		
		char read;
		
		read = (char) System.in.read();
		
		System.out.println("Leitura do caracter: " + read);
	}

}
