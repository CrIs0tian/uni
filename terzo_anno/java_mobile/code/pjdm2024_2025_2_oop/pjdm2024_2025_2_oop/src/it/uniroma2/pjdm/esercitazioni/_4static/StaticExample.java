package it.uniroma2.pjdm.esercitazioni._4static;

public class StaticExample {

	private int a;

	public static int counter = 0;

	private static int b = 26;
	
	public static Punto p;

	public static final int C = 10;
	
	/*
	 * DON'T TRY THIS AT HOME: IF THIS IS A PARMATER OF YOUR APPLICATION
	 * IT SHOULD BE SET IN A DEDICATED CONFIGURATION FILE
	 */
	public static final String username = "danilo";

	// Eseguito alla prima consultazione della CLASSE (non istanza) di StaticExample
	static {
		b = 27;
		p = new Punto(3, 4);
		p.setY(33);
		System.out.println("CIao, sono la classe StaticExample e sono appena stata caricata");
	}

	public StaticExample(int v) {
		this.a = v;
		counter++;
	}
	


	public static void main(String[] args) {

		System.out.println("Inizialmente b è uguale a " + StaticExample.b);
		
		StaticExample se = new StaticExample(3);
		StaticExample.b = 9;
		//This is incorrect, as b is static
		//se.b = 10;

		System.out.println("se.a = " + se.a);
		System.out.println("StaticExample.b = " + StaticExample.b);

		StaticExample se2 = new StaticExample(5);
		StaticExample.b = 10;

		System.out.println("se2.a = " + se2.a);
		System.out.println("StaticExample.b = " + StaticExample.b);
		
		System.out.println("Counter = " + counter);
		
		
		
	}

	public static int somma(int a, int b) {
		// The use of this is ILLEGAL!!!
		//return this.a + b; 		
		return a + b;
	}

	public void somma(int a1) {
		this.a = this.a + a1;
	}

}
