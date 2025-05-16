package it.uniroma2.courses.pjdm.entity;

import java.util.Objects;

public class Programmatore extends Dipendente {

	private String linguaggioConosciuto;

	public Programmatore(int matricola, String nome, String cognome, Data dataDiNascita, String linguaggioConosciuto) {
		super(matricola, nome, cognome, dataDiNascita);

		this.linguaggioConosciuto = linguaggioConosciuto;
	}

	public String getLinguaggioConosciuto() {
		return linguaggioConosciuto;
	}

	public void setLinguaggioConosciuto(String linguaggioConosciuto) {
		this.linguaggioConosciuto = linguaggioConosciuto;
	}

	public void sviluppaProgramma() {
		System.out.println("CHE BEL PROGRAMMA CHE STO IMPLEMENTANDO!");
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = super.hashCode();
		result = prime * result + Objects.hash(linguaggioConosciuto);
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
		Programmatore other = (Programmatore) obj;
		return Objects.equals(linguaggioConosciuto, other.linguaggioConosciuto);
	}

	@Override
	public String toString() {
		return "Programmatore [linguaggioConosciuto=" + linguaggioConosciuto + ", getNome()=" + getNome()
				+ ", getCognome()=" + getCognome() + ", getMatricola()=" + getMatricola() + ", getDataDiNascita()="
				+ getDataDiNascita() + ", toString()=" + super.toString() + ", getClass()=" + getClass() + "]";
	}

}
