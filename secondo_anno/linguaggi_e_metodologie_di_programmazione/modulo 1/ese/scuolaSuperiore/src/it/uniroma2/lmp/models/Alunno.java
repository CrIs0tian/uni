package it.uniroma2.lmp.models;
import java.time.*;




public class Alunno {
	private LocalDate DataNascita; 
	private String luogoNascita; 
	private String Nome; 
	private String Cognome; 
	private int AnnoIscrizione;
	
	public Alunno(LocalDate dataNascita, String luogoNascita, String nome, String cognome, int annoIscrizione) {
		super();
		this.setDataNascita(dataNascita);
		this.setLuogoNascita(luogoNascita);
		this.setAnnoIscrizione(annoIscrizione);
		this.setCognome(cognome);
		this.setNome(nome);
		}
	public LocalDate getDataNascita() {
		return DataNascita;
	}
	public void setDataNascita(LocalDate dataNascita) {
		DataNascita = dataNascita;
	}
	public String getLuogoNascita() {
		return luogoNascita;
	}
	public void setLuogoNascita(String luogoNascita) {
		this.luogoNascita = luogoNascita;
	}
	public String getNome() {
		return Nome;
	}
	public void setNome(String nome) {
		Nome = nome;
	}
	public String getCognome() {
		return Cognome;
	}
	public void setCognome(String cognome) {
		Cognome = cognome;
	}
	public int getAnnoIscrizione() {
		return AnnoIscrizione;
	}
	public void setAnnoIscrizione(int annoIscrizione) {
		AnnoIscrizione = annoIscrizione;
	}
	
	

}
