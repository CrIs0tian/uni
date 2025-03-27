package it.uniroma2.courses.pdjm.entity;

public class Dipendente {
	private String nome; 
	private String cognome; 
	private int matricola;
	
	
	public Dipendente(String nome, String cognome, int matricola) {
		// TODO Auto-generated constructor stub
		super();
		this.nome = nome;
		this.cognome = cognome;
		this.matricola = matricola;
	}
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getCognome() {
		return cognome;
	}
	public void setCognome(String cognome) {
		this.cognome = cognome;
	}
	public int getMatricola() {
		return matricola;
	}
	public void setMatricola(int matricola) {
		this.matricola = matricola;
	} 
	
	

}
