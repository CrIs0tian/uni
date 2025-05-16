package it.uniroma2.pjdm.controller;

import java.io.PrintStream;

import it.uniroma2.pjdm.entity.ListaDipendenti;
import it.uniroma2.pjdm.entity.exceptions.DuplicateIDException;

public class StatisticGenerator {

	private ListaDipendenti dipendenti;

	public StatisticGenerator(ListaDipendenti dipendenti) {
		this.dipendenti = dipendenti;
	}

	public void stampa() {
		stampa(System.out);
	}
	
	public void stampa(PrintStream ps) {

		ps.println("----------------");
		ps.println("Lista Dipendenti");
		ps.println("----------------");
		ps.println(dipendenti);
		ps.println("----------------");

		ps.println();

		ps.println("Numero Dipendenti:\t" + this.dipendenti.getNumeroDipendenti() + "\n");
		ps.println("Salario Medio:\t" + this.dipendenti.getSalarioMedio() + "\n");

		ps.println("Miglior Agente di Vendita:\t" + this.dipendenti.getAgenteConMaggiorNumeroClienti() + "\n");

		ps.println("Linguaggi Conosciuti in azienda:\t" + this.dipendenti.getInsiemeLinguaggiProgrammazione() + "\n");

		if (this.dipendenti.checkConsistenzaMatricole()) {
			ps.println("Non esistono matricole duplicate");
		} else
			ps.println("Attenzione: Esistono matricole duplicate!");

		try {
			this.dipendenti.checkConsistenzaMatricoleException();
		} catch (DuplicateIDException e) {
			ps.println("EXCEPTION:\t" + e.getMessage());
		}

	}

}
