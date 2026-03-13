import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader( System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer tokens;
    static long[] tree;
    static long[] lazy;
    static long[] arr;
    public static void main(String[] args) throws NumberFormatException, IOException {
        int N,M,K;
        int a,b,c;
        long d;

        N = Integer.parseInt(br.readLine());
        tree = new long[N*4];
        lazy = new long[N*4];
        arr = new long[N];
        tokens = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            arr[i] = Long.parseLong(tokens.nextToken());
        }

        build(0,0, N-1);

        M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            tokens = new StringTokenizer(br.readLine());
            a = Integer.parseInt(tokens.nextToken());
            b = Integer.parseInt(tokens.nextToken());
            if(a == 1){
                c = Integer.parseInt(tokens.nextToken());
                d = Integer.parseInt(tokens.nextToken());
                update(0, 0, N-1, b-1, c-1, d);
            }
            else {
                sb.append(query(0, 0, N-1, b-1, b-1)).append('\n');
            }
        }
        System.out.println(sb);
        // update(0,0,N-1,i, Long.parseLong(tokens.nextToken()));
    }

    public static void build(int node, int s, int e){
        if(s == e){
            tree[node] = arr[s];
            return;
        }

        int mid = (s+e)/2;
        build(node*2+1, s, mid);
        build(node*2+2, mid+1, e);
        tree[node] = tree[node*2+1] + tree[node*2+2];
    }

    public static void update(int node, int s, int e, int left, int right, long diff){
        propagation(node, s, e);

        if(right < s || e < left) return;
        if(left <= s && e <= right){
            lazy[node] += diff;
            propagation(node, s, e);
            return;
        }

        int mid = (s+e)/2;
        update(node*2+1, s, mid, left, right, diff);
        update(node*2+2, mid+1, e, left, right, diff);

        tree[node] = tree[node*2+1] + tree[node*2+2];
    }

    public static long query(int node, int s, int e, int left, int right){
        propagation(node, s, e);
        
        if(right < s || e < left) return 0;
        
        if(left <= s && e <= right) return tree[node];

        int mid = (s+e)/2;

        return query(node*2+1, s, mid, left, right) + query(node*2+2, mid+1, e, left, right);
    }

    public static void propagation(int node, int s, int e){
        if(lazy[node] == 0) return;

        tree[node] += (e - s + 1L) * lazy[node];

        if(s != e){
            lazy[node*2+1] += lazy[node];
            lazy[node*2+2] += lazy[node];
        }

        lazy[node] = 0;
    }
}
