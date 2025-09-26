package it.uniroma2.lmp;
import it.uniroma2.lmp.models.*;
import it.uniroma2.lmp.services.*;
import java.time.*;
import java.util.ArrayList;

public class test {

	public static void main(String[] args) {
		Alunno alunno1 = new Alunno(LocalDate.parse("2003-10-09"), "anagni", "cristian", "scursatone", 2025);
		Alunno alunno2 = new Alunno(LocalDate.parse("2001-05-11"), "ferentino", "francesco", "palombo", 2025);
		ArrayList<Alunno> listaAlunni = new ArrayList<Alunno>(); 
		Classe terzaC = new Classe(2003, 2025, 3 ,'c' , listaAlunni); 
		terzaC.AddStudent(alunno1);
		terzaC.AddStudent(alunno2);
		presideService preside = new presideService(); 
		preside.alunniRipetenti(terzaC);
		preside.numAlunni(terzaC);
		
		
		
		
		
		
		
		
		// TODO Auto-generated method stub

	}

}
