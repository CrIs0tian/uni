package it.uniroma2.pjdm.esercitazioni._5abstracts;

public class Programmatore extends Dipendente {

	public Programmatore(String nome, String cognome) {
		super(nome, cognome);
	}

	@Override
	public void doWork() {
		System.out.println("Sto programmando allegramente");
	}
	
	public void scriviCodice() {
		System.out.println("Che bel codice che sto sviluppando.");
	}

}
