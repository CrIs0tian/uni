package it.uniroma2.courses.pjdm;

import it.uniroma2.courses.pjdm.entity.Data;

public class MainData {
	public static void main(String[] args) {
		Data data1 = new Data(29, 13, 2024);
		System.out.println(data1);
		
		Data data2 = new Data(29, 12, 2031);
		System.out.println(data2);
		
		Data data3 = new Data(29, 2, 2023);
		System.out.println(data3);
		
		Data data4 = new Data(29, 2, 2024);
		System.out.println(data4);
		
		System.out.println(data4.getAnno());
	}
}
