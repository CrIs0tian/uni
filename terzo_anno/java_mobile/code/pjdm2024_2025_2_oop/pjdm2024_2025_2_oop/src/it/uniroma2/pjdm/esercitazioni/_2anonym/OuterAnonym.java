package it.uniroma2.pjdm.esercitazioni._2anonym;

public class OuterAnonym {

	public void stampaMessaggio() {
		System.out.println("ciao");
	}

	public static void main(String[] args) {
		OuterAnonym outerAnonym = new OuterAnonym();
		outerAnonym.stampaMessaggio();

		OuterAnonym outerAnonym2 = new OuterAnonym() {

			final private int a = 5;

			public void stampaMessaggio() {
				System.out.println(a + " hi");
			}
			
			@SuppressWarnings("unused")
			public void stampaMessaggioUsaEGetta() {
				System.out.println(a + " hi");
			}

		};
		outerAnonym2.stampaMessaggio();
//		outerAnonym2.stampaMessaggioUsaEGetta();
		
		// NON ho visibilità della funzione aggiunta: 
		// il "Puntatore" OuterAnonym non lo prevede
		// outerAnonym2.stampaMessaggioUsaEGetta();

	}

}
