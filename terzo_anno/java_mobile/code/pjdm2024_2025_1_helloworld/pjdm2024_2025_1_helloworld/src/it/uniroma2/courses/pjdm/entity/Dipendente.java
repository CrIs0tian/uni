package it.uniroma2.courses.pjdm.entity;

import java.util.Objects;

public class Dipendente {

	private String nome;
	private String cognome;
	private int matricola;
	private Data dataDiNascita;

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

	public Data getDataDiNascita() {
		return dataDiNascita;
	}

	public void setDataDiNascita(Data dataDiNascita) {
		this.dataDiNascita = dataDiNascita;
	}

	public Dipendente(int matricola, String nome, String cognome, Data dataDiNascita) {
		super();
		this.matricola = matricola;
		this.nome = nome;
		this.cognome = cognome;
		this.dataDiNascita = dataDiNascita;
	}

	@Override
	public int hashCode() {
		return Objects.hash(cognome, dataDiNascita, matricola, nome);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Dipendente other = (Dipendente) obj; // casting da obj a dipendente, (cosi accede agli altri parametri)
		return Objects.equals(cognome, other.cognome) && Objects.equals(dataDiNascita, other.dataDiNascita)
				&& matricola == other.matricola && Objects.equals(nome, other.nome);
	}

	@Override
	public String toString() {
		return "Dipendente [nome=" + nome + ", cognome=" + cognome + ", matricola=" + matricola + ", dataDiNascita="
				+ dataDiNascita + "]";
	}

}
