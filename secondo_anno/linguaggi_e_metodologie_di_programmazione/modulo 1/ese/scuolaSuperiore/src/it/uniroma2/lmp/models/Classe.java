package it.uniroma2.lmp.models;
import java.util.ArrayList;

public class Classe {
	private int AnnoStudentiRegolari; 
	private int AnnoCorso; 
	private int Sezione; 
	private char Nome; 
	private ArrayList<Alunno> listaStudenti;
	
	public Classe(int annoStudentiRegolari, int annoCorso, int sezione, char nome, ArrayList<Alunno> listaStudenti) {
		super();
		this.setAnnoMedioIscrizone(annoStudentiRegolari);
		this.setAnnoCorso(annoCorso);
		this.setSezione(sezione);
		this.setNome(nome);
		this.setListaStudenti(listaStudenti);
	}
	public int getAnnoMedioIscrizone() {
		return AnnoStudentiRegolari;
	}
	public void setAnnoMedioIscrizone(int annoMedioIscrizone) {
		AnnoStudentiRegolari = annoMedioIscrizone;
	}
	public int getAnnoCorso() {
		return AnnoCorso;
	}
	public void setAnnoCorso(int annoCorso) {
		AnnoCorso = annoCorso;
	}
	public int getSezione() {
		return Sezione;
	}
	public void setSezione(int sezione) {
		Sezione = sezione;
	}
	public char getNome() {
		return Nome;
	}
	public void setNome(char nome2) {
		Nome = nome2;
	}
	public ArrayList<Alunno> getListaStudenti() {
		return listaStudenti;
	}
	public void setListaStudenti(ArrayList<Alunno> listStudenti) {
		this.listaStudenti = listStudenti; 	
		} 
	public void AddStudent(Alunno alunno) {
		this.listaStudenti.add(alunno); 
		
	}
	
	
	
	
	
	
	

}
