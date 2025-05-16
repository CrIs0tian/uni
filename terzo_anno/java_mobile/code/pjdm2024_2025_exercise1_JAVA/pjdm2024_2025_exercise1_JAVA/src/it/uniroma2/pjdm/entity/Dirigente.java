package it.uniroma2.pjdm.entity;

import org.json.JSONException;
import org.json.JSONObject;

public class Dirigente extends Dipendente {

	private String nomeDivisioneControllata;

	// Opzionale, default = -1
	private static final int NESSUN_DIPENDENTE = -1;
	
	private int numeroDiependentiSottoposti = NESSUN_DIPENDENTE;

	public Dirigente(int matricola, String nome, String cognome, int salario, String nomeDivisioneControllata) {
		super(matricola, nome, cognome, salario);
		this.setNomeDivisioneControllata(nomeDivisioneControllata);
	}

	public Dirigente(int matricola, String nome, String cognome, int salario, String nomeDivisioneControllata,
			int numeroDiependentiSottoposti) {
		this(matricola, nome, cognome, salario, nomeDivisioneControllata);
		this.setNumeroDiependentiSottoposti(numeroDiependentiSottoposti);
	}

	@Override
	public JSONObject getJSONObject() throws JSONException {
		JSONObject jsonObject = super.getBasicJsonObject();
		jsonObject.put("nomeDivisioneControllata", nomeDivisioneControllata);
		jsonObject.put("numeroDiependentiSottoposti", numeroDiependentiSottoposti);
		return jsonObject;
	}

	public String getNomeDivisioneControllata() {
		return nomeDivisioneControllata;
	}

	public int getNumeroDiependentiSottoposti() {
		return numeroDiependentiSottoposti;
	}

	public void setNomeDivisioneControllata(String nomeDivisioneControllata) {
		this.nomeDivisioneControllata = nomeDivisioneControllata;
	}

	public void setNumeroDiependentiSottoposti(int numeroDiependentiSottoposti) {
		this.numeroDiependentiSottoposti = numeroDiependentiSottoposti;
	}
	
	@Override
	public String toString() {
		return super.toString() + ", nomeDivisioneControllata=" + nomeDivisioneControllata
				+ ", numeroDiependentiSottoposti=" + numeroDiependentiSottoposti;
	}

}
