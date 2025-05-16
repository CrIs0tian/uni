package it.uniroma2.courses.pdjm.ese.dipendenti.entity.exception;

public class DuplicateException extends Exception{ 
	private static final long serialVersionUID = 2375644004318093022L;
	public DuplicateException(String msg) {
		System.out.println(msg + "presente un duplicato"); 
		
		
	}

}
