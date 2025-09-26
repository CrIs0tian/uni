package it.uniroma2.lmp.services;
import it.uniroma2.lmp.models.*;
import java.util.*; 


public class presideService {
	public void numAlunni(Classe classe) {
		System.out.println("numero di alunni uguale a " + classe.getListaStudenti().size());
	}
	public void alunniRipetenti(Classe classe) {
		ArrayList<Alunno>listAlunni = classe.getListaStudenti(); 
		for (Alunno i: listAlunni) {
			if (i.getDataNascita().getYear() != classe.getAnnoMedioIscrizone()) {
				System.out.println("alunno " + i.getNome() +" "+  i.getCognome() + " ripetente da " + ( classe.getAnnoMedioIscrizone()- i.getDataNascita().getYear()) + " anni" ); 
				
			}
		}
		
	}

}
