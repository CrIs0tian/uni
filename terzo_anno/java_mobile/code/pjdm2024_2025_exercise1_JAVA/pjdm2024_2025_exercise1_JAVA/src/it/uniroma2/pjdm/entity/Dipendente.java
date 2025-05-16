package it.uniroma2.pjdm.entity;

import java.util.Objects;

import org.json.JSONException;
import org.json.JSONObject;

import it.uniroma2.pjdm.controller.JSONPrinter;

public abstract class Dipendente implements JSONPrinter {

	private int matricola;

	private String nome;

	private String cognome;

	private int salario;

	public Dipendente(int matricola, String nome, String cognome, int salario) {
		this.setMatricola(matricola);
		this.setNome(nome);
		this.setCognome(cognome);
		this.setSalario(salario);
	}

	// It is protected since to avoid that classes from other packages use it
	protected JSONObject getBasicJsonObject() throws JSONException {
		JSONObject jsonObject = new JSONObject();
		jsonObject.put("tipo", this.getClass().getSimpleName());
		jsonObject.put("matricola", matricola);
		jsonObject.put("nome", nome);
		jsonObject.put("cognome", cognome);
		jsonObject.put("salario", salario);
		return jsonObject;
	}

	public String getCognome() {
		return cognome;
	}

	public int getMatricola() {
		return matricola;
	}

	public String getNome() {
		return nome;
	}

	public int getSalario() {
		return salario;
	}

	public void setCognome(String cognome) {
		this.cognome = cognome;
	}

	public void setMatricola(int matricola) {
		this.matricola = matricola;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public void setSalario(int salario) {
		this.salario = salario;
	}

	@Override
	public String toString() {
		return "matricola=" + matricola + ", nome=" + nome + ", cognome=" + cognome + ", salario=" + salario;
	}

	@Override
	public int hashCode() {
		return Objects.hash(cognome, matricola, nome, salario);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Dipendente other = (Dipendente) obj;
		return Objects.equals(cognome, other.cognome) && matricola == other.matricola
				&& Objects.equals(nome, other.nome) && salario == other.salario;
	}

}
