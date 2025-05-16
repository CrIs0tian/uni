package it.uniroma2.courses.pjdm;

import java.util.TreeMap;

public class MainEsempioMap {

	public static void main(String[] args) {
		TreeMap<String, Integer> rubrica = new TreeMap<String, Integer>();
		
		rubrica.put("Danilo", Integer.parseInt("33398453"));
		rubrica.put("Mario", Integer.parseInt("34325235"));
		rubrica.put("Angela", Integer.parseInt("3243235"));
		
		System.out.println(rubrica.get("Angela"));
		
		System.out.println(rubrica);
		
		
 	}
	
}
