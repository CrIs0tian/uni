package it.uniroma2.lmp.exam.models;
import it.uniroma2.lmp.exam.enumaeration.Esito;

public class ProvaEsame {
	private ProvaParziale CompitoJava; 
	private ProvaParziale ComitoPython; 
	private ProvaParziale CompitoProlog; 
	private int VotoFinale; 
	private Studente Stud;
	private CoeffVoto CriteriVoto; 
	private Esito esitoEsame;
	public CoeffVoto getCriteriVoto() {
		return CriteriVoto;
	}
	public void setCriteriVoto(CoeffVoto criteriVoto) {
		CriteriVoto = criteriVoto;
	}
	public ProvaParziale getCompitoJava() {
		return CompitoJava;
	}
	public void setCompitoJava(ProvaParziale compitoJava) {
		CompitoJava = compitoJava;
	}
	public ProvaParziale getComitoPython() {
		return ComitoPython;
	}
	public void setComitoPython(ProvaParziale comitoPython) {
		ComitoPython = comitoPython;
	}
	public ProvaParziale getCompitoProlog() {
		return CompitoProlog;
	}
	public void setCompitoProlog(ProvaParziale compitoProlog) {
		CompitoProlog = compitoProlog;
	}
	public Studente getStud() {
		return Stud;
	}
	public void setStud(Studente stud) {
		Stud = stud;
	}
	public int getVotoFinale() {
		return VotoFinale;
	} 
	public void SetVotoFinale(int VotoOraleJava, int VotoOralePyPl, int PuntBonus) {
		float MediaPrimoCorso = (((this.CompitoJava.getVoto()*this.CriteriVoto.getCoeffVotoJava()) +VotoOraleJava)/(this.CriteriVoto.getCoeffVotoJava()+1) ); 
		float ProvaScrittaPyPl = ((this.ComitoPython.getVoto()*this.CriteriVoto.getCoeffVotoPython()+(this.CompitoProlog.getVoto()*this.CriteriVoto.getCoeffVotoProlog()))/(this.CriteriVoto.getCoeffVotoProlog()+this.CriteriVoto.getCoeffVotoPython()));
		float mediaSecondoCorso = (ProvaScrittaPyPl + VotoOralePyPl)/2;
		int VotoFinale = (int)((MediaPrimoCorso+mediaSecondoCorso) / 2) + PuntBonus; 
		
		this.VotoFinale = VotoFinale;
		
		
	}
	public Esito getEsitoEsame() {
		return esitoEsame;
	}
	public void setEsitoEsame() {
		if (this.VotoFinale < 18) {
			this.esitoEsame = Esito.BOCCIATO; 
		}
		else {
			this.esitoEsame = Esito.PROMOSSO; 
			
		}
		
	}
	public ProvaEsame(ProvaParziale compitoJava, ProvaParziale comitoPython, ProvaParziale compitoProlog, Studente stud, CoeffVoto criteriVoto, int VotoOraleJava, int ProvaOralePyPl, int PuntiBonus) {
		super();
		CompitoJava = compitoJava;
		ComitoPython = comitoPython;
		CompitoProlog = compitoProlog;
		Stud = stud;
		CriteriVoto = criteriVoto;
		this.SetVotoFinale(VotoOraleJava, VotoOraleJava, PuntiBonus);
		this.setEsitoEsame();
	}
	
	
	
	

}
