import java.util.*;

class Main {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int x = s.nextInt();
        for(int i = 0 ; i < n ; i++ ){
            int num = s.nextInt();
            if(num < x) System.out.print(num + " ");
        }
        
    }
}