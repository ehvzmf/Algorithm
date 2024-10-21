'''
https://www.acmicpc.net/problem/1051
백준 숫자 정사각형 
'''

n, m = map(int, input().split())
graph = []
for _ in range(n):
    tmp = list(input())
    graph.append(tmp)
    
s_max = min([n, m]) # 가능한 정사각형의 최대 변의 길이

def check(graph, s):
    flag = 0
    for i in range(len(graph)-s+1):
        for j in range(len(graph[0])-s+1):
            if graph[i][j] == graph[i+s-1][j] == graph[i][j+s-1] == graph[i+s-1][j+s-1]:
                flag = s*s
                return flag
                break # graph에서 s인 정사각형을 하나라도 찾으면 더 찾지 않음
    return 0 # 한 변의 길이가 s인 정사각형이 존재하지 않는 경우
                
answer = [] # 가능한 정사각형의 넓이 리스트
for lnth in range(1, s_max+1):
    if check(graph, lnth) != 0:
        answer.append(check(graph, lnth))
        
print(max(answer))