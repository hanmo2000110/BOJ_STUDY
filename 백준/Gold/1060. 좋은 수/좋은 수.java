import java.io.*;
import java.util.*;

public class Main {
	
	static class LuckySet {
		int num;
		int start;
		int end;
		int isFinish;
		
		public LuckySet(int num) {
			this.num = num;
			this.isFinish = 0;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int L = Integer.parseInt(br.readLine());
		LuckySet[] ls = new LuckySet[L+1];
		ls[0] = new LuckySet(0);
		
		st = new StringTokenizer(br.readLine());
		for (int i=1; i<=L; i++) {
			ls[i] = new LuckySet(Integer.parseInt(st.nextToken()));
		}
		int N = Integer.parseInt(br.readLine());
		
		Arrays.sort(ls, new Comparator<LuckySet>() {
			public int compare(LuckySet l1, LuckySet l2) {
				return l1.num - l2.num;
			}
		});
		
		////////////////////////// 입력
		
		// 1 - unlucky 구간이 0인 경우
		ArrayList<Integer> al = new ArrayList<>();
		for (int i=1; i<=L; i++) {
			al.add(ls[i].num); // lucky set 값 정답에 넣기
		}
		for (int i=0; i<L; i++) {
			int diff = ls[i+1].num - ls[i].num;
			
			if (diff == 1) { // 값 차이 1이면 해당 lucky set 탐색할 필요 X 
				ls[i].isFinish = 1; 
			} else if (diff == 2) { // 값 차이 2면 num+1 정답에 넣기
				al.add(ls[i].num + 1);
				ls[i].isFinish = 1;
			} else { // 값 차이 3 이상이면 start, end 세팅
				ls[i].start = ls[i].num + 1;
				ls[i].end = ls[i+1].num - 1;
			}
		}
		al.sort(null);
		
		// 2 - unlucky 구간이 0보다 크면서 유한한 경우
		PriorityQueue<Integer> pq = new PriorityQueue<>();
		Queue<Integer> q = new LinkedList<>();
		boolean isChange = true;
		while (isChange && al.size()<N) {
			isChange = false;
			
			long min = Long.MAX_VALUE;
			for (int i=0; i<L; i++) {
				if (ls[i].isFinish == 1) // 탐색하지 않을 곳이면 패스
					continue;
				
				int pre = ls[i].start - ls[i].num - 1;
				int next = ls[i+1].num - ls[i].start;
				long val = (long)pre*next + next-1; // unlucky 구간 개수 계산
				
				if (val < min) {
					q.clear();
					q.add(i);
					
					min = val;
					isChange = true;
				} else if (val == min) { 
					q.add(i); // 최소 구간 개수가 같으면 한꺼번에 정답에 넣기 위해 큐에 넣음
				}
			}
			
			if (isChange) {
				while (!q.isEmpty()) {
					int idx = q.poll();

					// 우선순위가 같은 경우 작은 순서로 넣기 위해 우선순위 큐 사용
					pq.add(ls[idx].start);
					if (ls[idx].start != ls[idx].end)
						pq.add(ls[idx].end);
					
					ls[idx].start++;
					ls[idx].end--;
					
					if (ls[idx].start > ls[idx].end)
						ls[idx].isFinish = 1;
				}
				
				while (!pq.isEmpty()) {
					al.add(pq.poll());
				}
			}
		}
		
		// 3 - unlucky 구간이 무한한 경우
		for (int i=ls[L].num+1; al.size()<N; i++) {
			al.add(i);
		}
		
		// print
		StringBuilder sb = new StringBuilder();
		for (int i=0; i<N; i++) {
			sb.append(al.get(i)).append(' ');
		}
		System.out.println(sb);
	}
}