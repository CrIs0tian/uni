package it.uniroma2.pjdm.esercitazioni._5abstracts;

import java.util.ArrayList;

public class Main {

	public static void main(String[] args) {
		
	
		ArrayList<Dipendente> lista = new ArrayList<Dipendente>();
		// QUESTO DI SOPRA E' UNA VERSIONE DINAMICA DI
		//Dipendente[] array = new Dipendente[4];

		Dirigente capo = new Dirigente("Mario", "Rossi", "Dip. Vendite");
		Dipendente nerd = new Programmatore("Mattero", "Gialli");
		//nerd.scriviCodice(); NON FUNZIONA!!! Perche'?
		
		//Dipendente agDiVendita = new AgenteDiVendita("Carlo", "Bianchi");
		//NON POSSO INSTANZIARE AGENTIDIVENDITA POICHE' ASTRATTO
		
		
		// Posso instanziare una classe astratta ma deve essere implementata
		// come una classe anonima
		// DA USARE CON CAUTELA
		Dipendente stranoDipendenteAnonimo = new Dipendente("Luigi", "Bianchi") {

			@Override
			public void doWork() {
				System.out.println("sono uno strano dipendente di tipo 1");

			}
		};

		// DO NOT TRY THIS AT HOME
		Dipendente stranoDipendenteAnonimo2 = new Dipendente("Gianluca", "Neri") {

			@Override
			public void doWork() {
				System.out.println("sono uno strano dipendente di tipo 2");
			}
		};

		lista.add(capo);
		lista.add(nerd);
		lista.add(stranoDipendenteAnonimo);
		lista.add(stranoDipendenteAnonimo2);

		for (int i = 0; i < lista.size(); i++) {
			Dipendente tmp = lista.get(i);

			System.out.println(tmp.getClass());

			if (tmp instanceof Dirigente) {
				System.out.println("E' un capo!!!");
				
				Dirigente dirigente = (Dirigente) tmp;
				dirigente.assegnaPromozione();
			}

			tmp.doSomething();
			tmp.doWork();
			System.out.println("\n");
		}

		// list.add(new Dirigente());
		// list.add(new Programmatore());
		//
		// for(Dipendente d: list){
		// d.doWork();
		// }
	}

}
