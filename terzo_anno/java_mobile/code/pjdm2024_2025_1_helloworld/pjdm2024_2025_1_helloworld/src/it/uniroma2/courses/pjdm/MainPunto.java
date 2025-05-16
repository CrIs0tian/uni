package it.uniroma2.courses.pjdm;

import it.uniroma2.courses.pjdm.entity.Punto;

public class MainPunto {

	public static void main(String[] args) {
		Punto p = new Punto(3.0, 7.0);
		
		System.out.println(p);
		System.out.println(p.distanzeDallOrigine());
	}
	
}
