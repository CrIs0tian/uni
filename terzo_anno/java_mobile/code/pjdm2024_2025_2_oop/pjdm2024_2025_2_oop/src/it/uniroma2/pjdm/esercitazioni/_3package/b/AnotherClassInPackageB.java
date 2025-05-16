package it.uniroma2.pjdm.esercitazioni._3package.b;

import it.uniroma2.pjdm.esercitazioni._3package.a.ClassInPackageA;

public class AnotherClassInPackageB {

	public static void main(String[] args) {
		ClassInPackageA classInPackageA = new ClassInPackageA();
		
		System.out.println(classInPackageA.getPublicVariable());
		// THIS METHOD IS PROTECTED!!!! 
		//System.out.println(classInPackageA.getProtectedVariable());
	}
	
}
