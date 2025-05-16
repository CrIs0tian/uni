package it.uniroma2.pjdm.controller;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

import it.uniroma2.pjdm.entity.AgenteDiVendita;
import it.uniroma2.pjdm.entity.Dipendente;
import it.uniroma2.pjdm.entity.Dirigente;
import it.uniroma2.pjdm.entity.ListaDipendenti;
import it.uniroma2.pjdm.entity.Programmatore;
import it.uniroma2.pjdm.entity.exceptions.DipendenteTypeException;
import it.uniroma2.pjdm.entity.exceptions.ProvvigioneException;

/**
 * This class implements the method(s) for reading a ListaDipendenti from file
 *
 * @author Danilo Croce
 */
public class Reader {

	/**
	 * This methods read a ListaDipendenti from a CSV file
	 * 
	 * @param inputFilePath the path of the input CSV file
	 * 
	 * @return the list of "Dipendenti"
	 * @throws IOException
	 * @throws DipendenteTypeException 
	 */
	public static ListaDipendenti readFromCSV(String inputFilePath) throws IOException, DipendenteTypeException {
		File file = new File(inputFilePath); //per 'dire' al programma che questo è un file
		ListaDipendenti res = new ListaDipendenti();

		BufferedReader in = new BufferedReader(new InputStreamRkeader(new FileInputStream(file)));

		String str;

		while ((str = in.readLine()) != null) {
			String[] split = str.split(";");
			int matricola = Integer.parseInt(split[0]);
			String nome = split[1];
			String cognome = split[2];
			int salario = Integer.parseInt(split[3]);
			String tipo = split[4];

			Dipendente dipendente = null;

			switch (tipo) {
			case "Dirigente":
				String nomeDivisioneControllata = split[5];

				if (split.length == 7) {
					int numeroDiependentiSottoposti = Integer.parseInt(split[6]);
					dipendente = new Dirigente(matricola, nome, cognome, salario, nomeDivisioneControllata,
							numeroDiependentiSottoposti);
				} else {
					dipendente = new Dirigente(matricola, nome, cognome, salario, nomeDivisioneControllata);
				}
				res.add(dipendente);
				break;
			case "Programmatore":
				String linguaggioConosciuto = split[5];
				dipendente = new Programmatore(matricola, nome, cognome, salario, linguaggioConosciuto);

				res.add(dipendente);
				break;
			case "AgenteDiVendita":
				try {
					float provvigione = Float.parseFloat(split[5]);
					int numeroClienti = Integer.parseInt(split[6]);
					dipendente = new AgenteDiVendita(matricola, nome, cognome, salario, provvigione, numeroClienti);
					res.add(dipendente);
				} catch (ProvvigioneException e) {
					System.err.println("PROBLEMA: SKIPPING AgenteDiVendita\t" + e.getMessage());
					e.printStackTrace();
				}
				break;
			default:
				throw new DipendenteTypeException(tipo);
			}

		}

		in.close();
		return res;
	}
}
