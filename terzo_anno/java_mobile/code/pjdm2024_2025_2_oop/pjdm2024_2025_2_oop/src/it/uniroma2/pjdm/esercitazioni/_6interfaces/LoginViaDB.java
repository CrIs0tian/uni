package it.uniroma2.pjdm.esercitazioni._6interfaces;

public class LoginViaDB implements Login {

	private String dbIP;

	private int doPort;

	public LoginViaDB(String dbIP, int doPort) {
		super();
		this.dbIP = dbIP;
		this.doPort = doPort;
	}

	public boolean checkConnection(String addredd) {
		return false;
	}

	@Override
	public void checkPassword(String pwd) {
		System.out.println("Sono un check passwork di LoginViaDB");

	}

	public String getDbIP() {
		return dbIP;
	}

	public int getDoPort() {
		return doPort;
	}

	@Override
	public int getID(String Name) {
		// TODO Auto-generated method stub
		return 0;
	}

	public void setDbIP(String dbIP) {
		this.dbIP = dbIP;
	}

	public void setDoPort(int doPort) {
		this.doPort = doPort;
	}
}
