package it.uniroma2.pjdm.entity.exceptions;

public class DipendenteTypeException extends Exception {

	private static final long serialVersionUID = 2375644004318093022L;

	public DipendenteTypeException(String msg) {
		super("Problema con il tipo specificato del dipendente:\t" + msg);
	}

}
