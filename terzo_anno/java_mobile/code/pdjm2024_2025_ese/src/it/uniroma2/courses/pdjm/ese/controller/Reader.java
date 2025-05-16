package it.uniroma2.courses.pdjm.ese.controller;
import java.io.*;
import it.uniroma2.courses.pdjm.ese.dipendenti.entity.*; 
import it.uniroma2.courses.pdjm.ese.dipendenti.entity.exception.TypeException; 
import it.uniroma2.courses.pdjm.ese.dipendenti.entity.exception.provviggioneException;





/*classe reader 
 * 
 * implementa un reader che legge una listadipendenti su un file 
 * 
 * parametri : stringa contente il percorso del file 
 * 
 * return: arraylist di dipendenti 
 * potrebbe lanciare: IOException, TypeException */

public class Reader {
	public static listaDipendenti read(String pathToFile) throws IOException, TypeException{ 
		/*1.aprire lo stream di input*/ 
		File file = new File(pathToFile); //per dire al codice che pathtofile è un file 
		listaDipendenti LDipendenti = new listaDipendenti();
		BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(file))); 
		/*why questo? dobbiamo leggere un file csv (binario), leggerlo come testo cosi da poterli gestire 
		 * */
		
		
		
		
		
		
	}
	

}
