'''
https://level.goorm.io/exam/138223/18%ED%9A%8C-e-pper-%EA%B8%B0%EC%B6%9C-%ED%95%A9%EC%8A%B9%ED%83%9D%EC%8B%9C%EC%9A%94%EA%B8%88/quiz/1
구름 - 합승택시 경유지 추가 (플로이드워셜, 그래프)
'''

import sys
#본 시험에서는 solution 코드와 별도로 필요한 함수만 작성합니다.

INF = 1e7 #최대 n-1개의 간선을 지나게 됨

def fillGraph(n, fares):
	graph = [[INF] * (n+1) for _ in range(n+1)]
	
	for i in range(1, n+1):
		graph[i][i] = 0
		
	for u, v, w in fares:
		graph[u][v] = w
		graph[v][u] = w
		
	return graph

def floydWarshall(graph, n):
	for k in range(1, n+1):
		for i in range(1, n+1):
			for j in range(1, n+1):
				graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

def solution(n, s, a, b, fares, lay):
#들여쓰기에 주의하면서 필요한 코드를 작성하세요
	answer = INF
	graph = fillGraph(n, fares)
	floydWarshall(graph, n)
		
	for i in range(1, n+1):
		answer = min(answer, graph[s][lay]+graph[lay][i]+graph[i][a]+graph[i][b])
				
	return answer

if __name__ == "__main__":
    input = sys.stdin.readline
    n, s, a, b, c = map(int, input().split())

    # 테스트 케이스 개수 : 9
    i = 9;
    fares=[list(map(int, input().split())) for _ in range(i)]
    answer = solution(n, s, a, b, fares, c)
    print(answer)
