package it.uniroma2.pjdm.esercitazioni._5abstracts;

public class Dirigente extends Dipendente {

	private String nomeDipartimento;
	
	public Dirigente(String nome, String cognome, String nomeDipartimento) {
		super(nome, cognome);
		this.nomeDipartimento = nomeDipartimento;
	}

	public String getNomeDipartimento() {
		return nomeDipartimento;
	}

	public void setNomeDipartimento(String nomeDipartimento) {
		this.nomeDipartimento = nomeDipartimento;
	}

	public void assegnaPromozione() {
		System.out.println("Sei stato promosso");
	}

	@Override
	public void doWork() {
		System.out.println("Sto dirigendo la company bellamente.");
	}

}
