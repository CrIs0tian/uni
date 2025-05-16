package it.uniroma2.pjdm.esercitazioni._6interfaces;

public class MainInterface {

	public static void main(String[] args) {
		//Login login = new LoginViaDB("127.0.0.1", 3);
		Login login = new LoginViaFile();


		login.checkPassword("012345");
		login.getID("Danilo");

		// Non si usa perchè è utilizzabile solo per un oggetto di tipo LoginViaFile

		// DO AT YOUR OWN RISK
		if (login instanceof LoginViaFile) {
			System.out.println("Sono nell'instanceof");
			LoginViaFile loginViaFile = (LoginViaFile) login;
			loginViaFile.azioneRichiestaDaFile();
		}

	}

}
