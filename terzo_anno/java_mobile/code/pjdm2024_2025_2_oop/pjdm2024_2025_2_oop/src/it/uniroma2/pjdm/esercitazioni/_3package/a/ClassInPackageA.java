package it.uniroma2.pjdm.esercitazioni._3package.a;

public class ClassInPackageA {

	private int publicVariable;
	
	private int protectedVariable;

	public ClassInPackageA() {
		this.publicVariable = 3;
		this.protectedVariable = 5;
	}

	protected int getProtectedVariable() {
		return protectedVariable;
	}

	public int getPublicVariable() {
		return publicVariable;
	}

	protected void setProtectedVariable(int protectedVariable) {
		this.protectedVariable = protectedVariable;
	}
	
	public void setPublicVariable(int publicVariable) {
		this.publicVariable = publicVariable;
	}
	
}
