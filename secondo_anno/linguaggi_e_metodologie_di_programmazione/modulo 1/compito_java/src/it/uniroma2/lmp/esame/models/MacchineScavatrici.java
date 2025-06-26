package it.uniroma2.lmp.esame.models;
import it.uniroma2.lmp.esame.enumerables.*;

public class MacchineScavatrici extends Auto{
	private int coppiaBraccio; 
	private DirezioneBraccio dirBraccio;
	public MacchineScavatrici(String modello, Colore colore, TipoAntifurto antifurto, String targa) {
		super(modello, colore, antifurto, targa);
		// TODO Auto-generated constructor stub
	}
	public int getCoppiaBraccio() {
		return coppiaBraccio;
	}
	public void setCoppiaBraccio(int coppiaBraccio) {
		this.coppiaBraccio = coppiaBraccio;
	}
	public DirezioneBraccio getDirBraccio() {
		return dirBraccio;
	}
	public void setDirBraccio(DirezioneBraccio dirBraccio) {
		this.dirBraccio = dirBraccio;
	}
	

}
