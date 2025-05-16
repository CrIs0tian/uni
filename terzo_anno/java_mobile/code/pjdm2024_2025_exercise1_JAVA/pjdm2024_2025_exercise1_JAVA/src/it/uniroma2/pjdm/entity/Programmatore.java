package it.uniroma2.pjdm.entity;

import java.util.Objects;

import org.json.JSONException;
import org.json.JSONObject;

/**
 * 
 * This class implements an istance of a programmer.
 * 
 * @author Danilo Croce
 */
public class Programmatore extends Dipendente {

	/**
	 * The programming language known to the programmer 
	 */
	private String linguaggioConosciuto;

	/**
	 * The only used constructor
	 * 
	 * @param matricola The programmer's ID
	 * @param nome The programmer's name
	 * @param cognome The programmer's surname
	 * @param salario The programmer's salary
	 * @param linguaggioConosciuto The programming language known to the programmer
	 */
	public Programmatore(int matricola, String nome, String cognome, int salario, String linguaggioConosciuto) {
		super(matricola, nome, cognome, salario);
		this.setLinguaggioConosciuto(linguaggioConosciuto);
	}

	@Override
	public JSONObject getJSONObject() throws JSONException {
		JSONObject jsonObject = super.getBasicJsonObject();
		jsonObject.put("linguaggioConosciuto", linguaggioConosciuto);
		return jsonObject;
	}

	/**
	 * @return The programming language known to the programmer
	 */
	public String getLinguaggioConosciuto() {
		return linguaggioConosciuto;
	}

	/**
	 * @param linguaggioConosciuto The programming language known to the programmer
	 */
	public void setLinguaggioConosciuto(String linguaggioConosciuto) {
		this.linguaggioConosciuto = linguaggioConosciuto;
	}

	@Override
	public String toString() {
		return super.toString() + ", linguaggioConosciuto=" + linguaggioConosciuto;
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

	

	

}
