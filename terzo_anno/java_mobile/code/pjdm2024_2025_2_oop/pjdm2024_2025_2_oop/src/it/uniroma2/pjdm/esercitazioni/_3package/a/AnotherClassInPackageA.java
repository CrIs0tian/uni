package it.uniroma2.pjdm.esercitazioni._3package.a;

public class AnotherClassInPackageA {

	public static void main(String[] args) {
		ClassInPackageA classInPackageA = new ClassInPackageA();
		
		System.out.println(classInPackageA.getPublicVariable());
		System.out.println(classInPackageA.getProtectedVariable());
	}
	
}
