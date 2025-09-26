package it.uniroma2.lmp.exam.models;

public class CoeffVoto {
	private float CoeffVotoProlog; 
	private float CoeffVotoJava; 
	private float CoeffVotoPython;
	public float getCoeffVotoProlog() {
		return CoeffVotoProlog;
	}
	public void setCoeffVotoProlog(float coeffVotoProlog) {
		CoeffVotoProlog = coeffVotoProlog;
	}
	public float getCoeffVotoJava() {
		return CoeffVotoJava;
	}
	public void setCoeffVotoJava(float coeffVotoJava) {
		CoeffVotoJava = coeffVotoJava;
	}
	public float getCoeffVotoPython() {
		return CoeffVotoPython;
	}
	public void setCoeffVotoPython(float coeffVotoPython) {
		CoeffVotoPython = coeffVotoPython;
	}
	public CoeffVoto(float coeffVotoProlog, float coeffVotoJava, float coeffVotoPython) {
		super();
		CoeffVotoProlog = coeffVotoProlog;
		CoeffVotoJava = coeffVotoJava;
		CoeffVotoPython = coeffVotoPython;
	} 
	
	

}
