package it.uniroma2.courses.pdjm.entity;

public class Dirigente extends Dipendente{ 
	private String orarioDiLavoro; 

	public Dirigente(String nome, String cognome, int matricola, String orariodilavoro)
	{
		super(nome, cognome, matricola);
		this.orarioDiLavoro = orariodilavoro; 
		
	}
	public String getOrarioDiLavoro() {
		return orarioDiLavoro;
	}
	public void setOrarioDiLavoro(String orarioDiLavoro) {
		this.orarioDiLavoro = orarioDiLavoro;
	}
	
}
