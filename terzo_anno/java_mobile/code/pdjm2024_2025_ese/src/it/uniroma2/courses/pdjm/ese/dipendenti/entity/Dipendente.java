package it.uniroma2.courses.pdjm.ese.dipendenti.entity;

import java.util.Objects;

import it.uniroma2.courses.pdjm.ese.dipendenti.entity.exception.CredentialException;

public class Dipendente {
	private int matricola;
	private String nome; 
	private String cognome; 
	private int salarioMensile; 
	
	public Dipendente(String nome, String cognome, int salarioMensile, int matricola) {
		
		try {
			if (cognome == null || nome == null || salarioMensile == 0) {
				throw new CredentialException();
			}
			this.setNome(nome);
			this.setCognome(cognome); 
			this.setSalarioMensile(salarioMensile);
			this.setMatricola(matricola);		
		} catch (CredentialException exc) {
			System.out.println(exc.toString());
		}	
	}




	@Override
	public String toString() {
		return "Dipendente [nome=" + nome + ", cognome=" + cognome + ", salarioMensile=" + salarioMensile + "]";
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

	public int getSalarioMensile() {
		return salarioMensile;
	}

	public void setSalarioMensile(int salarioMensile) {
		this.salarioMensile = salarioMensile;
	}

	public int getMatricola() {
		return matricola;
	}

	public void setMatricola(int matricola) {
		this.matricola = matricola;
	}

	@Override
	public int hashCode() {
		return Objects.hash(cognome, matricola, nome, salarioMensile, matricola);
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
				&& Objects.equals(nome, other.nome) && salarioMensile == other.salarioMensile;
	}
	

}
