package it.uniroma2.lmp.esame.models;
import it.uniroma2.lmp.esame.enumerables.*;

public class VeicoloPesante extends Auto{
	private int altezza; 
	private int peso;
	public VeicoloPesante(String modello, Colore colore, TipoAntifurto antifurto, String targa) {
		super(modello, colore, antifurto, targa);
		// TODO Auto-generated constructor stub
	}
	public int getAltezza() {
		return altezza;
	}
	public void setAltezza(int altezza) {
		this.altezza = altezza;
	}
	public int getPeso() {
		return peso;
	}
	public void setPeso(int peso) {
		this.peso = peso;
	} 
	
	
	
}
