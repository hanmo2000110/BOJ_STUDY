import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        int[] dp = new int[31];
        int sum = 0;
        dp[0] = 1;
        dp[2] = 3;
        int n = Integer.parseInt(br.readLine());

        if(n%2!=0) {
            System.out.println(0);
            return;
        }
        else {
            for(int  i = 4 ; i < n+1 ; i+=2){
                sum += dp[i-4]*2;
                dp[i] = dp[i-2]*3 + sum;
            }
        }

        System.out.println(dp[n]);
    }
}