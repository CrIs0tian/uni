package it.uniroma2.courses.pjdm;

import it.uniroma2.courses.pjdm.entity.ArchivioDipendenti;
import it.uniroma2.courses.pjdm.entity.Data;
import it.uniroma2.courses.pjdm.entity.Dipendente;
import it.uniroma2.courses.pjdm.entity.Dirigente;
import it.uniroma2.courses.pjdm.entity.Programmatore;

public class MainDipendenti {

	public static void main(String[] args) {

		ArchivioDipendenti listaDipendenti = new ArchivioDipendenti();

		listaDipendenti.add(new Dirigente(001, "Danilo", "Croce", new Data(20, 07, 1982), "fulltime"));

		System.out.println("Numero Dipendenti:\t" + listaDipendenti.size());

		System.out.println("C'è lo stesso oggetto?:\t"
				+ listaDipendenti.contains(new Dirigente(001, "Danilo", "Croce", new Data(20, 07, 1982), "fulltime")));
		System.out.println("C'è un oggetto leggermente diverso?:\t"
				+ listaDipendenti.contains(new Dirigente(001, "Danilo", "Croce", new Data(21, 07, 1982), "fulltime")));

		listaDipendenti.add(new Dirigente(002, "Mario", "Rossi", new Data(10, 06, 1996), "partime"));
		listaDipendenti.add(new Programmatore(002, "Luigi", "Bianchi", new Data(28, 02, 1995), "java"));

		System.out.println("Numero Dipendenti:\t" + listaDipendenti.size());

		for (Dipendente d : listaDipendenti) {
			System.out.println(d);
		}

		System.out.println("Va tutto bene senza duplicazioni?\t" + listaDipendenti.checkDuplicazioniMatricole());

	}

}
