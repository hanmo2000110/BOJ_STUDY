import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int count = a + b + c;
		
		if(count <= 21) {
			System.out.println("1");
		}else {
			System.out.println("0");
		}
		sc.close();
	}
}