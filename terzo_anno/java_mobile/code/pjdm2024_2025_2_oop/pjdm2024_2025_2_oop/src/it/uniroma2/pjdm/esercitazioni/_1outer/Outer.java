package it.uniroma2.pjdm.esercitazioni._1outer;

public class Outer {

	private int a;

	private String messaggio = "Nella classe ";

	public Outer() {
		this.a = 2;
	}

	public void setA(int a) {
		this.a = a;
	}

	public int getA() {
		return a;
	}

	public String getMessaggio() {
		return messaggio;
	}

	public void setMessaggio(String string) {
		this.messaggio = string;
	}

	public void stampaMessaggio() {
		System.out.println(this.messaggio + " esterna\t a = " + this.a);
	}

	public class Inner {

		private boolean bool;

		public Inner() {
			this.bool = true;
			a = 5; //this.a = 5 DOES NOT WORK!!, poichè non c'è un rapporto di sottoclasse/superclasse
		}

		public boolean isBool() {
			return bool;
		}

		public void setBool(boolean bool) {
			this.bool = bool;
		}

		public void stampaMessaggio() {
			System.out.println(messaggio + " interna\t a = " + a + " and bool = " + bool);
		}
	}

	public static void main(String[] args) {
		Outer outer = new Outer();
		outer.stampaMessaggio();
		
		System.out.println("\nOra creo La classe interna\n");
		
		//NON SI PUO' FARE, NON HO IL PUNTATORE
		//System.out.println(outer.Inner); 

		Outer.Inner inner1 = outer.new Inner(); // comando per istanziare classe interna, che DIPENDE totalmente dalla classe esterna
		inner1.stampaMessaggio();
		outer.stampaMessaggio();

		outer.setMessaggio("sto facendo hacking");
		outer.stampaMessaggio();
		inner1.stampaMessaggio();
	}

}
