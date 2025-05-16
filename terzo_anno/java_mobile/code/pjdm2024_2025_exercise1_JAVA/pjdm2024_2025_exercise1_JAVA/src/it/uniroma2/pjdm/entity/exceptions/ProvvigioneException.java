package it.uniroma2.pjdm.entity.exceptions;

public class ProvvigioneException extends Exception {

	private static final long serialVersionUID = -6886087605566571890L;

	public ProvvigioneException(String msg) {
		super(msg);
	}

	public ProvvigioneException() {
		super("Problema con provvigione, ma non so di quanto...");
	}

}
