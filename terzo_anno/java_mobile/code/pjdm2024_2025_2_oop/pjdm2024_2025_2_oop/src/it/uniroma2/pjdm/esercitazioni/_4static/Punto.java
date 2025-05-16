package it.uniroma2.pjdm.esercitazioni._4static;

public class Punto {

	private int x;
	
	private int y;
	
	public static final Punto origine = new Punto(0, 0);

	public Punto(int x, int y) {
		super();
		this.x = x;
		this.y = y;
	}

	public int getX() {
		return x;
	}

	public int getY() {
		return y;
	}
	
	public void setY(int y) {
		this.y=y;
	}
	
}
