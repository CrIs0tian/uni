package it.uniroma2.courses.pdjm.ese.dipendenti.entity;

import java.util.Objects;

import it.uniroma2.courses.pdjm.ese.dipendenti.entity.exception.provviggioneException;



public class AgenteDiVendita extends Dipendente{
	double provvigione; 
	int numClienti = -1;
	public AgenteDiVendita(String nome, String cognome, int salarioMensile,int matricola,  double provvigione, int numClienti) throws provviggioneException {
		super(nome, cognome, salarioMensile, matricola);
		this.setProvvigione(provvigione); 
		this.setNumClienti(numClienti);
		
	}
	public double getProvvigione() {
		return provvigione;
	}
	public void setProvvigione(double provvigione) throws provviggioneException{
		if (provvigione < 0.03f || provvigione > 0.5f) {
			throw new provviggioneException("errore");
		}else {
			this.provvigione = provvigione;
			
		}
	}
	public int getNumClienti() {
		return numClienti;
	}
	public void setNumClienti(int numClienti) {
		this.numClienti = numClienti;
	}
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = super.hashCode();
		result = prime * result + Objects.hash(numClienti, provvigione);
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
		AgenteDiVendita other = (AgenteDiVendita) obj;
		return numClienti == other.numClienti
				&& Double.doubleToLongBits(provvigione) == Double.doubleToLongBits(other.provvigione);
	}
	@Override
	public String toString() {
		return "AgenteDiVendita [provvigione=" + provvigione + ", numClienti=" + numClienti + ", toString()="
				+ super.toString() + ", getNome()=" + getNome() + ", getCognome()=" + getCognome()
				+ ", getSalarioMensile()=" + getSalarioMensile() + ", getMatricola()=" + getMatricola()
				+ ", getClass()=" + getClass() + "]";
	} 
	
	
	
}
