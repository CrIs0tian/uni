package it.uniroma2.pjdm.entity.exceptions;

public class DuplicateIDException extends Exception {

	private static final long serialVersionUID = -3558224031680066113L;

	public DuplicateIDException(String msg) {
		super(msg);
	}
}
