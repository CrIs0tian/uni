package it.uniroma2.courses.pdjm.ese.dipendenti.entity;

public class Dirigente extends Dipendente{
	private String divisoneControllata;
	private static int NESSUNDIPENDENTE = -1;  //static = valore uguale per qualsiasi istanza della classe
	private int numDipendenti = NESSUNDIPENDENTE;
	

	public Dirigente(String nome, String cognome, int salarioMensile, int matricola, String divisioneControllata) {
		super(nome,cognome,salarioMensile, matricola);
		this.setDivisoneControllata(divisioneControllata);
	}
	public Dirigente(String nome, String cognome, int salarioMensile, int matricola, String divisioneControllata, int numDipendenti) {
		super(nome, cognome, salarioMensile, matricola); 
		this.setNumDipeSottoposti(numDipendenti);
	}
	

		
	

	@Override
	public String toString() {
		return "Dirigente [divisoneControllata=" + divisoneControllata + ", numDipeSottoposti=" + numDipendenti
				+ "]";
	}


	public String getDivisoneControllata() {
		return divisoneControllata;
	}

	public void setDivisoneControllata(String divisoneControllata) {
		this.divisoneControllata = divisoneControllata;
	}

	public int getNumDipeSottoposti() {
		return this.numDipendenti;
	}

	public void setNumDipeSottoposti(int numDipendenti) {
		this.numDipendenti = numDipendenti;
	} 
	

}
