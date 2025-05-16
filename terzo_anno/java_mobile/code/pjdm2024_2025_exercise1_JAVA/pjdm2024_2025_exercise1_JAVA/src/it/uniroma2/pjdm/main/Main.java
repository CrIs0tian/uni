package it.uniroma2.pjdm.main;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintStream;
import java.io.UnsupportedEncodingException;

import org.json.JSONException;

import it.uniroma2.pjdm.controller.Reader;
import it.uniroma2.pjdm.controller.StatisticGenerator;
import it.uniroma2.pjdm.entity.ListaDipendenti;
import it.uniroma2.pjdm.entity.exceptions.DipendenteTypeException;

/**
 * 
 * A class useful to execute this program in a command line
 * 
 * @author Danilo Croce
 *
 */
public class Main {

	/**
	 * The main method
	 * 
	 * @param args
	 */
	public static void main(String[] args) {

		if (args.length != 2) {
			System.err.println("ERROR: you must provide the following parameters");
			System.err.println("\tinputFilePath:\tthe path of the input CSV");
			System.err.println("\toutputFilePath:\tthe output file name");
			return;
		}

		String inputFilePath = args[0];
		String outputFilePath = args[1];

		ListaDipendenti dipendenti = null;

		try {
			dipendenti = Reader.readFromCSV(inputFilePath);
		} catch (IOException e1) {
			System.err.println("Non riesco ad aprire il file " + inputFilePath);
			e1.printStackTrace();
			// important to stop running ... if needed
			return;
		} catch (DipendenteTypeException e1) {
			e1.printStackTrace();
			return;
		}

		StatisticGenerator statisticGenerator = new StatisticGenerator(dipendenti);

		try {
			PrintStream outputPs = new PrintStream(outputFilePath, "utf8");

			statisticGenerator.stampa(outputPs);

			statisticGenerator.stampa(System.out);
			// o in alternativa
			// statisticaDipendenti.stampa();
			
			outputPs.close();

		} catch (FileNotFoundException e) {
			System.err.println("Non riesco ad aprire il file " + outputFilePath);
			e.printStackTrace();
			// important to stop running ... if needed
			return;
		} catch (UnsupportedEncodingException e) {
			System.err.println("Non riesco ad aprire il file " + outputFilePath);
			e.printStackTrace();
			// important to stop running ... if needed
			return;
		}

		// OPTIONAL LET'S CONVERT IT IN JSON
		try {
			System.out.println("\n=======================\n");
			System.out.println("\nHERE A JSON CONVERSION\n");
			System.out.println(dipendenti.getJSONString());
		} catch (JSONException e) {
			System.err.println("Problem when converting the list in JSON");
			e.printStackTrace();
		}

		System.out.println("\nBYE BYE");

	}

}
