package it.uniroma2.lmp.exam.models;

public class Studente {
	private int Matricola; 
	private String Nome; 
	private String Congnome;
	
	
	public Studente(int matricola, String nome, String congnome) {
		super();
		Matricola = matricola;
		Nome = nome;
		Congnome = congnome;
	}
	public int getMatricola() {
		return Matricola;
	}
	public void setMatricola(int matricola) {
		Matricola = matricola;
	}
	public String getNome() {
		return Nome;
	}
	public void setNome(String nome) {
		Nome = nome;
	}
	public String getCongnome() {
		return Congnome;
	}
	public void setCongnome(String congnome) {
		Congnome = congnome;
	} 
	

}
