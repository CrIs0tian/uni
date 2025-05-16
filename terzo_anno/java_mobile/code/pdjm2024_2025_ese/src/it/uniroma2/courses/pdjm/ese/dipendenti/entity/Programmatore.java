package it.uniroma2.courses.pdjm.ese.dipendenti.entity;

import it.uniroma2.courses.pdjm.ese.dipendenti.entity.exception.CredentialException;

public class  Programmatore extends Dipendente{
	private String LinguaggioConosciuto; 

	public Programmatore(String nome, String cognome, int salarioMensile, int matricola, String linguaggioConosciuto) {
		super(nome, cognome, salarioMensile, matricola);
		try {
			if(linguaggioConosciuto == null || linguaggioConosciuto.isEmpty()) {
				throw new CredentialException();
			}
			this.setLinguaggioConosciuto(linguaggioConosciuto);
			
		}catch (CredentialException exc){
			System.out.println(exc.toString()); 
		}
		
	}

	public String getLinguaggioConosciuto() {
		return LinguaggioConosciuto;
	}

	public void setLinguaggioConosciuto(String linguaggioConosciuto) {
		LinguaggioConosciuto = linguaggioConosciuto;
	}
	
	
	

}
