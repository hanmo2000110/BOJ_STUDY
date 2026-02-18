import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[][] board;
    static int[][] islandId;
    static boolean[][] visited;

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static final int INF = 1_000_000_000;

    static class Edge implements Comparable<Edge> {
        int u, v, w;
        Edge(int u, int v, int w) {
            this.u = u;
            this.v = v;
            this.w = w;
        }
        @Override
        public int compareTo(Edge o) {
            return this.w - o.w;
        }
    }

    static class DSU {
        int[] parent;
        int[] rank;

        DSU(int n) {
            parent = new int[n + 1];
            rank = new int[n + 1];
            for (int i = 0; i <= n; i++) parent[i] = i;
        }

        int find(int x) {
            if (parent[x] == x) return x;
            return parent[x] = find(parent[x]);
        }

        boolean union(int a, int b) {
            a = find(a);
            b = find(b);
            if (a == b) return false;

            if (rank[a] < rank[b]) {
                int tmp = a;
                a = b;
                b = tmp;
            }
            parent[b] = a;
            if (rank[a] == rank[b]) rank[a]++;
            return true;
        }
    }

    static void bfsLabel(int sx, int sy, int id) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{sx, sy});
        visited[sx][sy] = true;
        islandId[sx][sy] = id;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0];
            int y = cur[1];

            for (int d = 0; d < 4; d++) {
                int nx = x + dx[d];
                int ny = y + dy[d];

                if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
                if (visited[nx][ny]) continue;
                if (board[nx][ny] == 0) continue; // 바다

                visited[nx][ny] = true;
                islandId[nx][ny] = id;
                q.offer(new int[]{nx, ny});
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        board = new int[N][M];
        islandId = new int[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 1) 섬 라벨링
        int islandCnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] == 1 && !visited[i][j]) {
                    islandCnt++;
                    bfsLabel(i, j, islandCnt);
                }
            }
        }

        if (islandCnt <= 1) {
            System.out.println(0);
            return;
        }

        // 2) 간선 추출 (섬 간 최소 다리 길이)
        int[][] dist = new int[islandCnt + 1][islandCnt + 1];
        for (int i = 1; i <= islandCnt; i++) {
            Arrays.fill(dist[i], INF);
            dist[i][i] = 0;
        }

        for (int x = 0; x < N; x++) {
            for (int y = 0; y < M; y++) {
                if (islandId[x][y] == 0) continue;
                int from = islandId[x][y];

                for (int d = 0; d < 4; d++) {
                    int nx = x + dx[d];
                    int ny = y + dy[d];
                    int len = 0;

                    while (0 <= nx && nx < N && 0 <= ny && ny < M) {
                        if (islandId[nx][ny] == from) break; // 자기 섬 만나면 무효

                        if (islandId[nx][ny] == 0) {
                            len++;
                            nx += dx[d];
                            ny += dy[d];
                            continue;
                        }

                        // 다른 섬 도착
                        int to = islandId[nx][ny];
                        if (to != from && len >= 2) {
                            if (len < dist[from][to]) {
                                dist[from][to] = len;
                                dist[to][from] = len;
                            }
                        }
                        break;
                    }
                }
            }
        }

        List<Edge> edges = new ArrayList<>();
        for (int i = 1; i <= islandCnt; i++) {
            for (int j = i + 1; j <= islandCnt; j++) {
                if (dist[i][j] != INF) {
                    edges.add(new Edge(i, j, dist[i][j]));
                }
            }
        }

        // 3) Kruskal
        Collections.sort(edges);
        DSU dsu = new DSU(islandCnt);

        int total = 0;
        int used = 0;
        for (Edge e : edges) {
            if (dsu.union(e.u, e.v)) {
                total += e.w;
                used++;
                if (used == islandCnt - 1) break;
            }
        }

        if (used != islandCnt - 1) System.out.println(-1);
        else System.out.println(total);
    }
}