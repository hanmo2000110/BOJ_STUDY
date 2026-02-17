import java.io.*;
import java.util.*;

/**
 * BOJ 17471 게리맨더링
 * 완전탐색(부분집합) + 연결성 검사(BFS)
 */
public class Main {
    static int N;
    static int[] people;
    static List<Integer>[] graph;
    static boolean[] selected; // true면 A 선거구, false면 B 선거구
    static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine().trim());
        people = new int[N + 1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            people[i] = Integer.parseInt(st.nextToken());
        }

        graph = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) graph[i] = new ArrayList<>();

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            int cnt = Integer.parseInt(st.nextToken());
            for (int j = 0; j < cnt; j++) {
                int v = Integer.parseInt(st.nextToken());
                graph[i].add(v);
            }
        }
        selected = new boolean[N + 1];
        // 부분집합 생성: 각 구역을 A(true) 또는 B(false)에 배정
        subset(1);

        System.out.println(answer == Integer.MAX_VALUE ? -1 : answer);
    }

    static void subset(int idx) {
        if (idx == N + 1) {
            evaluate();
            return;
        }

        // idx를 A에 넣는 경우
        selected[idx] = true;
        subset(idx + 1);

        // idx를 B에 넣는 경우
        selected[idx] = false;
        subset(idx + 1);
    }

    static void evaluate() {
        int aCount = 0, bCount = 0;
        int aStart = -1, bStart = -1;
        int aSum = 0, bSum = 0;

        // A/B 인원수, 시작점, 인구수 합 계산
        for (int i = 1; i <= N; i++) {
            if (selected[i]) {
                aCount++;
                aSum += people[i];
                if (aStart == -1) aStart = i;
            } else {
                bCount++;
                bSum += people[i];
                if (bStart == -1) bStart = i;
            }
        }

        // 한쪽이 비어있으면 불가능
        if (aCount == 0 || bCount == 0) return;

        // A, B 각각 연결인지 검사
        int aVisited = bfs(aStart, true);   // A 선거구 내부만 BFS
        if (aVisited != aCount) return;

        int bVisited = bfs(bStart, false);  // B 선거구 내부만 BFS
        if (bVisited != bCount) return;

        // 둘 다 연결이면 인구 차이로 정답 갱신
        answer = Math.min(answer, Math.abs(aSum - bSum));
    }

    /**
     * start에서 시작해서 같은 선거구(isA) 내 노드만 BFS
     * 방문한 노드 수 반환
     */
    static int bfs(int start, boolean isA) {
        Queue<Integer> q = new ArrayDeque<>();
        boolean[] visited = new boolean[N + 1];

        visited[start] = true;
        q.offer(start);
        int count = 1;

        while (!q.isEmpty()) {
            int cur = q.poll();

            for (int next : graph[cur]) {
                if (visited[next]) continue;
                // 같은 선거구가 아니면 못 감
                if (selected[next] != isA) continue;

                visited[next] = true;
                q.offer(next);
                count++;
            }
        }

        return count;
    }
}