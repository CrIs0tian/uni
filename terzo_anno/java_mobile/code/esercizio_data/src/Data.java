
public class Data {
	private int giorno; 
	private int mese; 
	private int anno; 
	public Data(int g, int m, int a) {
		giorno = 0; 
		mese = 0; 
		anno = 0;
		setAnno(a); 
		setMese(m); 
		setGiorno(g);
		
	}
	public void setAnno(int a) {
		if (a<=2025) { 
			anno = a; 
		}
		else {
			System.out.println("inserire un anno valido, rincoglionito");
		}
	}
	public void setMese(int m) {
		if (m <= 12 && m >=1) {
			mese=m;
		}
		else {
			System.out.println("inserire un mese valido, umano inutile"); 
			
		}
	}
	public void setGiorno(int g) {
		
	}
	public int getGiorno() {
		return giorno;
		
	}
	public int getMese() {
		return mese;
		
	}
	public int getAnno() {
		return anno;
		
	}
	
	

}
