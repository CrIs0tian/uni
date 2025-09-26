package it.uniroma2.lmp.exam.models;
import it.uniroma2.lmp.exam.enumaeration.*;

public class ProvaParziale {
	private TypeCompito ArgCompito; 
	private int Voto;
	private Studente studente;
	public TypeCompito getArgCompito() {
		return ArgCompito;
	}
	public void setArgCompito(TypeCompito argCompito) {
		ArgCompito = argCompito;
	}
	public int getVoto() {
		return Voto;
	}
	public void setVoto(int voto) {
		Voto = voto;
	}
	public Studente getStudente() {
		return studente;
	}
	public void setStudente(Studente studente) {
		this.studente = studente;
	}
	public ProvaParziale(TypeCompito argCompito, int voto, Studente studente) {
		super();
		ArgCompito = argCompito;
		Voto = voto;
		this.studente = studente;
	} 
	
	
	
	

}
