package it.uniroma2.pjdm.entity;

import java.util.ArrayList;
import java.util.HashSet;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import it.uniroma2.pjdm.controller.JSONPrinter;
import it.uniroma2.pjdm.entity.exceptions.DuplicateIDException;

public class ListaDipendenti extends ArrayList<Dipendente> {

	private static final long serialVersionUID = -7755179547095617766L;

	public boolean checkConsistenzaMatricole() {
		HashSet<Integer> matricole = new HashSet<Integer>();
		for (Dipendente dipendente : this) {
			if (matricole.contains(dipendente.getMatricola()))
				return false;
			matricole.add(dipendente.getMatricola());
		}
		return true;
	}

	public void checkConsistenzaMatricoleException() throws DuplicateIDException {
		HashSet<Integer> matricole = new HashSet<Integer>();
		for (Dipendente dipendente : this) {
			if (matricole.contains(dipendente.getMatricola())) {
				String msg = "Attenzione: Esistono matricole duplicate: caused by\t" + dipendente.toString();
				throw new DuplicateIDException(msg);
			}
			matricole.add(dipendente.getMatricola());
		}
	}

	public AgenteDiVendita getAgenteConMaggiorNumeroClienti() {
		int maxClienti = 0;

		AgenteDiVendita migliorAgenteDiVendita = null;

		for (Dipendente dipendente : this) {
			if (dipendente instanceof AgenteDiVendita) {
				AgenteDiVendita agenteDiVendita = (AgenteDiVendita) dipendente;
				if (agenteDiVendita.getNumeroClienti() > maxClienti) {
					maxClienti = agenteDiVendita.getNumeroClienti();
					migliorAgenteDiVendita = agenteDiVendita;
				}
			}
		}

		return migliorAgenteDiVendita;
	}

	public HashSet<String> getInsiemeLinguaggiProgrammazione() {
		HashSet<String> res = new HashSet<String>();
		for (Dipendente dipendente : this) {
			if (dipendente instanceof Programmatore) {
				Programmatore programmatore = (Programmatore) dipendente;
				res.add(programmatore.getLinguaggioConosciuto());
			}
		}
		return res;
	}

	public String getJSONString() throws JSONException {
		JSONArray jsonArray = new JSONArray();

		for (Dipendente dipendente : this) {
			JSONPrinter jsonPrinter = (JSONPrinter) dipendente;
			JSONObject jsonObject = jsonPrinter.getJSONObject();
			jsonArray.put(jsonObject);
		}
		// The parameter 1 is used to indent the produced string
		return jsonArray.toString(1);
	}

	public float getNumeroDipendenti() {
		return (float) this.size();
	}

	public float getSalarioMedio() {
		float res = 0;
		for (Dipendente dipendente : this) {
			res += dipendente.getSalario();
		}
		return res /= getNumeroDipendenti();
	}

	@Override
	public String toString() {
		String res = "";
		for (Dipendente dipendente : this) {
			res += dipendente.getClass().getSimpleName() + ":\t" + dipendente.toString() + "\n";
		}
		return res;
	}
}
