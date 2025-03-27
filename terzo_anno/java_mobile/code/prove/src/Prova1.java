
public class Prova1 {
	public static void main(String args[]) {
		int i = 1; 
		while(i<=10) {
			System.out.println("provaWhile");
			i ++; 
		}
		int b = 10; 
		do {
			System.out.println(b);
		} while (b<10);
		int c = 3; 
		switch(c) {
		case 3:
			System.out.println("vada a fare");
		break;
		case 4: {
			System.out.println("nel");
			System.out.println("culo");
			}
		break;		
		}
		int f = 0; 
		do {
			f++; 
			if (f == 5) {
				continue;
			}
			System.out.println(f);
		} while (f<=10);
		
	}

}
