package it.uniroma2.pjdm.entity;

import org.json.JSONException;
import org.json.JSONObject;

import it.uniroma2.pjdm.entity.exceptions.ProvvigioneException;

public class AgenteDiVendita extends Dipendente {

	private float provvigione;

	private int numeroClienti;

	public AgenteDiVendita(int matricola, String nome, String cognome, int salario, float provvigione,
			int numeroClienti) throws ProvvigioneException {
		super(matricola, nome, cognome, salario);
		this.setProvvigioni(provvigione);
		this.setNumeroClienti(numeroClienti);
	}

	@Override
	public JSONObject getJSONObject() throws JSONException {
		JSONObject jsonObject = super.getBasicJsonObject();
		jsonObject.put("provvigione", provvigione);
		jsonObject.put("numeroClienti", numeroClienti);
		return jsonObject;
	}

	public int getNumeroClienti() {
		return numeroClienti;
	}

	public float getProvvigioni() {
		return provvigione;
	}

	public void setNumeroClienti(int numeroClienti) {
		this.numeroClienti = numeroClienti;
	}

	public void setProvvigioni(float provvigione) throws ProvvigioneException {
		if (provvigione < 0.05f || provvigione > 0.3f)
			throw new ProvvigioneException("Problema con provvigione:\t" + provvigione);
		this.provvigione = provvigione;
	}

	@Override
	public String toString() {
		return super.toString() + ", provvigione=" + provvigione + ", numeroClienti=" + numeroClienti;
	}
}
