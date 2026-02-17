import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 과목 수
        int M = Integer.parseInt(st.nextToken()); // 선수 관계 수

        List<Integer>[] graph = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) graph[i] = new ArrayList<>();

        int[] indegree = new int[N + 1];
        int[] semester = new int[N + 1];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            graph[A].add(B);
            indegree[B]++;
        }

        Queue<Integer> q = new ArrayDeque<>();

        // 선수 과목이 없는 과목은 1학기
        for (int i = 1; i <= N; i++) {
            if (indegree[i] == 0) {
                q.offer(i);
                semester[i] = 1;
            }
        }

        // 위상정렬
        while (!q.isEmpty()) {
            int cur = q.poll();

            for (int next : graph[cur]) {
                indegree[next]--;

                // next는 cur 다음 학기 이상이어야 함
                semester[next] = Math.max(semester[next], semester[cur] + 1);

                if (indegree[next] == 0) {
                    q.offer(next);
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= N; i++) {
            sb.append(semester[i]).append(' ');
        }

        System.out.println(sb.toString().trim());
    }
}