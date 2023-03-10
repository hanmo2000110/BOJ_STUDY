import java.util.List;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		int N = Integer.parseInt(st.nextToken());	// 듣도 못한 사람의 수
		int M = Integer.parseInt(st.nextToken());	// 보도 못한 사람의 수
		
		Set<String> hs = new HashSet<String>();	// 듣도 못한 사람 저장
		List<String> list = new ArrayList<String>();
		for(int i=0; i<N; i++)	
			hs.add(bf.readLine());	// 듣도 못한 사람 저장
		
		for(int i=0; i<M; i++) {
			String str = bf.readLine();
			// 보도 못한 사람이 듣도 못한 사람에 있을경우 => list에 저장
			if(hs.contains(str)) 	list.add(str);
		}
		
		Collections.sort(list);
		System.out.println(list.size());	// 듣도 보도 못한 사람의 수 => list의 크기
		for(int i=0; i<list.size(); i++)
			System.out.println(list.get(i));
		
		bf.close();
	}

}