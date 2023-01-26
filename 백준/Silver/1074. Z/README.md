# [Silver I] Z - 1074 

[문제 링크](https://www.acmicpc.net/problem/1074) 

### 성능 요약

메모리: 241112 KB, 시간: 108 ms

### 분류

분할 정복(divide_and_conquer), 재귀(recursion)

### 문제 설명

<p>한수는 크기가 2<sup>N</sup> × 2<sup>N</sup>인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.</p>

<p style="text-align:center"><img alt="" src="" style="width: 100px; height: 99px;"></p>

<p>N > 1인 경우, 배열을 크기가 2<sup>N-1</sup> × 2<sup>N-1</sup>로 4등분 한 후에 재귀적으로 순서대로 방문한다.</p>

<p>다음 예는 2<sup>2</sup> × 2<sup>2</sup> 크기의 배열을 방문한 순서이다.</p>

<p style="text-align:center"><img alt="" src="" style="width: 250px; height: 252px;"></p>

<p>N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.</p>

<p>다음은 N=3일 때의 예이다.</p>

<p style="text-align:center"><img alt="" src="" style="width: 533px; height: 535px;"></p>

### 입력 

 <p>첫째 줄에 정수 N, r, c가 주어진다.</p>

### 출력 

 <p>r행 c열을 몇 번째로 방문했는지 출력한다.</p>

### 접근법 :
분할 정복으로 풀면 된다.
해보겠다
사등분 해서 왼쪽 위 오른쪽 위 왼쪽 아래 오른쪽 아래 순으로 체크하며
결과값을 누적시킨다.

여러 시도를 해보았다 
재귀를 안 쓰고 풀어보려고 했는데 가능은 해보이는데 재귀가 더 쉬워 보여서 중간에 갈아엎었다
조건문 논리 짤 때 분명 쉬운 조건문인데 잠을 덜 자서인지 집중이 잘 안되고 헷갈려서 삽질을 많이 했다
알고리즘 문제는 정신 말짱할 때 풀어야겠다...
분할 정복이 어떤 느낌인지 알 수 있어서 좋았다