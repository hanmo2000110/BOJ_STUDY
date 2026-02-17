import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[][] map;
    static int[][] owner; // 바다/땅 칸이 어느 섬에서 확장됐는지
    static int[][] dist;  // 해당 칸까지 바다를 몇 칸 건넜는지
    static final int[] dx = {-1, 1, 0, 0};
    static final int[] dy = {0, 0, -1, 1};

    static class Node {
        int x, y;
        Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine().trim());
        map = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 1) 섬 라벨링: 1(땅)들을 2,3,4...로 구분
        int islandId = 2;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j] == 1) {
                    labelIsland(i, j, islandId++);
                }
            }
        }

        // 2) 멀티소스 BFS 준비
        owner = new int[N][N];
        dist = new int[N][N];
        for (int i = 0; i < N; i++) {
            Arrays.fill(dist[i], -1); // 방문 전 = -1
        }

        Queue<Node> q = new ArrayDeque<>();

        // 모든 땅 칸을 시작점으로 큐에 넣는다.
        // (외곽만 넣어도 되지만, 전체 넣어도 정답/복잡도 O(N^2)로 충분)
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (map[i][j] > 1) { // 라벨링된 섬
                    owner[i][j] = map[i][j];
                    dist[i][j] = 0;
                    q.offer(new Node(i, j));
                }
            }
        }

        int answer = Integer.MAX_VALUE;

        // 3) 멀티소스 BFS
        while (!q.isEmpty()) {
            Node cur = q.poll();

            for (int d = 0; d < 4; d++) {
                int nx = cur.x + dx[d];
                int ny = cur.y + dy[d];

                if (nx < 0 || ny < 0 || nx >= N || ny >= N) continue;

                // 아직 아무 섬도 도달하지 않은 칸이면
                if (dist[nx][ny] == -1) {
                    dist[nx][ny] = dist[cur.x][cur.y] + 1;
                    owner[nx][ny] = owner[cur.x][cur.y];
                    q.offer(new Node(nx, ny));
                }
                // 이미 누군가 도달한 칸인데, 다른 섬에서 온 경우 -> 만남!
                else if (owner[nx][ny] != owner[cur.x][cur.y]) {
                    int candidate = dist[nx][ny] + dist[cur.x][cur.y];
                    answer = Math.min(answer, candidate);
                }
            }
        }

        System.out.println(answer);
    }

    // BFS로 하나의 섬(연결된 땅 덩어리)을 같은 번호(id)로 칠함
    static void labelIsland(int sx, int sy, int id) {
        Queue<Node> q = new ArrayDeque<>();
        q.offer(new Node(sx, sy));
        map[sx][sy] = id;

        while (!q.isEmpty()) {
            Node cur = q.poll();

            for (int d = 0; d < 4; d++) {
                int nx = cur.x + dx[d];
                int ny = cur.y + dy[d];

                if (nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
                if (map[nx][ny] != 1) continue; // 아직 라벨링 안 된 땅만

                map[nx][ny] = id;
                q.offer(new Node(nx, ny));
            }
        }
    }
}