package it.uniroma2.courses.pdjm.ese.dipendenti.entity;
import java.util.ArrayList;

import java.util.HashSet;

import it.uniroma2.courses.pdjm.ese.dipendenti.entity.exception.DuplicateException;

/*dobbiamo implementare le rischieste del punto 2. 
 * inanzitutto, prima di implementare il reader, ci servirebbe qualcosa che controlli che i dipendenti che aggiungiamo non abbiamo la stessa matricola:
 *  se lo hanno, la classe deve generare una eccezzione  */

public class listaDipendenti extends ArrayList<Dipendente>{
	private static final long serialVersionUID = -7755179547095l;
	public void checkDuplicateExcep() throws DuplicateException{
		HashSet<Integer> matricole = new HashSet<Integer>(); 
		for(Dipendente dipendente:this) { //scorre tutti gli oggetti dipendenti nella lista
			if(matricole.contains(dipendente.getMatricola())){
				throw new DuplicateException("errore :"); 
			} 
			matricole.add(dipendente.getMatricola()); 
			
		}
		
	}
	

}
