package it.uniroma2.pjdm.esercitazioni._7singleton;

public class SingletonExample {

	// To implement a Singleton I need a declaration of the target object made
	// static
	private static SingletonExample ex = null;

	private int counter = 0;

	private SingletonExample() {
		this.counter = 0;
	}

	public static SingletonExample getInstance() {
		if (ex == null) {
			ex = new SingletonExample();
			System.out.println("First time:\t" + ex.getCounter());
			ex.incCounter();
		} else {
			System.out.println("Other times:\t" + ex.getCounter());
			// NON E' OBBLIGATORIO MODIFICARE L'OGGETTO
			// VOLENDO, POTREI SOLO RESTITUIRLO
			ex.incCounter();
			return ex;
		}

		return ex;
	}

	private void incCounter() {
		this.counter++;

	}

	public static void main(String[] args) {
		SingletonExample ex = SingletonExample.getInstance();

		ex = SingletonExample.getInstance();
		ex = SingletonExample.getInstance();
		ex = SingletonExample.getInstance();
		ex = SingletonExample.getInstance();
		ex = SingletonExample.getInstance();

		System.out.println(ex);
	}

	public int getCounter() {
		return counter;
	}

}
