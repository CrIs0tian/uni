package it.uniroma2.lmp.cardreader.model;

public class Negozio extends AttivitaCommerciale {

	String merceVenduta;

	/**
	 * @param inizioAttivita
	 * @param sede
	 * @param partitaIVA
	 */
	public Negozio(int inizioAttivita, String sede, String partitaIVA, String merceVenduta) {
		super(inizioAttivita, sede, partitaIVA);
		this.merceVenduta = merceVenduta;
	}

	public String getMerceVenduta() {
		return merceVenduta;
	}

	public void setMerceVenduta(String merceVenduta) {
		this.merceVenduta = merceVenduta;
	}
	
	public String toString(){
		return "negozio\n" + "in attività dal" + inizioAttivita + "\npartita IVA: " + partitaIVA + "\nsede: " + sede + "\nmerce venduta: " + merceVenduta;

	}

}
