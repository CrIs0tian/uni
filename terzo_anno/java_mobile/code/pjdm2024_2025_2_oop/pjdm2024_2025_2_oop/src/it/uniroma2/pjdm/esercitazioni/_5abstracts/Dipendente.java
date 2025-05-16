package it.uniroma2.pjdm.esercitazioni._5abstracts;

public abstract class Dipendente {

	private String nome;
	private String cognome;
	
	public Dipendente(String nome, String cognome) {
		this.setCognome(cognome);
		this.setNome(nome);
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getNome() {
		return nome;
	}

	public abstract void doWork();

	public String getCognome() {
		return cognome;
	}

	public void setCognome(String cognome) {
		this.cognome = cognome;
	}
	
	public void doSomething(){
		System.out.println("Sto facendo qualcosa");
	}

	
	
}
