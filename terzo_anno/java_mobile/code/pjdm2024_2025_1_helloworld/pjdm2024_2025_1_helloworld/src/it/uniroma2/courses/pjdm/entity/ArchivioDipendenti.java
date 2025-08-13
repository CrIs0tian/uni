 	package it.uniroma2.courses.pjdm.entity;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.TreeSet;

public class ArchivioDipendenti extends ArrayList<Dipendente> {
	/*arraylist: classe che implementa le liste dinamiche, può essere utilizzato solo per contenere oggetti*/

	private static final long serialVersionUID = 7934520366144610305L;

	public boolean checkDuplicazioniMatricole() {

		int size = this.size();

		HashSet<Integer> insiemeMatricole = new HashSet<Integer>();
		TreeSet<Integer> insiemeMatricoleOrdinato = new TreeSet<Integer>();

		for (Dipendente d : this) {
			insiemeMatricole.add(d.getMatricola());
			insiemeMatricoleOrdinato.add(d.getMatricola());
		}

		System.out.println(insiemeMatricole);
		System.out.println(insiemeMatricoleOrdinato);

		if (size == insiemeMatricole.size()) {
			return true;
		} else {
			return false;
		}

	}

}
