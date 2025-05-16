package it.uniroma2.courses.pjdm.entity;

import java.util.Objects;

public class Dirigente extends Dipendente {

	private String orarioDiLavoro;

	public Dirigente(int matricola, String nome, String cognome, Data dataDiNascita, String orarioDiLavoro) {
		super(matricola, nome, cognome, dataDiNascita);

		this.orarioDiLavoro = orarioDiLavoro;
	}
	
	

	public String getOrarioDiLavoro() {
		return orarioDiLavoro;
	}

	public void setOrarioDiLavoro(String orarioDiLavoro) {
		this.orarioDiLavoro = orarioDiLavoro;
	}

	public void daGliOrdini() {
		System.out.println("FAI QUESTO!!! SUBITO!!");
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = super.hashCode();
		result = prime * result + Objects.hash(orarioDiLavoro);
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (!super.equals(obj))
			return false;
		if (getClass() != obj.getClass())
			return false;
		Dirigente other = (Dirigente) obj; /*anche qui casting, ma serve per confrontare le variabili presenti solo nella superclasse (ecco a cosa serve il casting)*/
		return Objects.equals(orarioDiLavoro, other.orarioDiLavoro);
	}

	@Override
	public String toString() {
		return "Dirigente [orarioDiLavoro=" + orarioDiLavoro + ", getNome()=" + getNome() + ", getCognome()="
				+ getCognome() + ", getMatricola()=" + getMatricola() + ", getDataDiNascita()=" + getDataDiNascita()
				+ ", toString()=" + super.toString() + ", getClass()=" + getClass() + "]";
	}

}
