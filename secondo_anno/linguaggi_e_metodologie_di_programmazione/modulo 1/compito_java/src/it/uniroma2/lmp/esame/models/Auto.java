package it.uniroma2.lmp.esame.models;

import it.uniroma2.lmp.esame.enumerables.*;

public class Auto {
	private String modello;
	private Colore colore; 
	private TipoAntifurto antifurto; 
	private String targa; 
	private int velocità; 
	private int accelerazione;
	private boolean antifurtoAttivo;
	private float GpsX; 
	private float GpsY; 
	public Auto(String modello, Colore colore, TipoAntifurto antifurto, String targa) {
		
		this.modello = modello;
		this.colore = colore;
		this.antifurto = antifurto;
		this.targa = targa;
		
	}
	
	
	public float getGpsX() {
		return GpsX;
	}
	public void setGpsX(float gpsX) {
		GpsX = gpsX;
	}
	public float getGpsY() {
		return GpsY;
	}
	public void setGpsY(float gpsY) {
		GpsY = gpsY;
	}
	
	public String getModello() {
		return modello;
	}
	
	public Colore getColore() {
		return colore;
	}
	
	public TipoAntifurto getAntifurto() {
		return antifurto;
	}
	
	public String getTarga() {
		return targa;
	}
	
	public int getVelocità() {
		return velocità;
	}
	public void setVelocità(int velocità) {
		this.velocità = velocità;
	}
	public int getAccelerazione() {
		return accelerazione;
	}
	public void setAccelerazione(int accelerazione) {
		this.accelerazione = accelerazione;
	}


	public boolean isAntifurtoAttivo() {
		return antifurtoAttivo;
	}


	public void setAntifurtoAttivo(boolean antifurtoAttivo) {
		this.antifurtoAttivo = antifurtoAttivo;
	} 
	
	
	
	
	
	

}
