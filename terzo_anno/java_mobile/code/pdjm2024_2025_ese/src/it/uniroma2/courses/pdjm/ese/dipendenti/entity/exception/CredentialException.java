package it.uniroma2.courses.pdjm.ese.dipendenti.entity.exception;

public class CredentialException extends Exception{ 
	private static final long serialVersionUID = 1L;
	public CredentialException () {
		super("errore : "); 
	
	}
	public String toString() {
		return getMessage() + "credenziali mancanti"; 
	}

}
