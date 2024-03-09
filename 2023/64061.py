'''

https://school.programmers.co.kr/learn/courses/30/lessons/64061?language=python3
Programmers. 64061 - 크레인 인형뽑기 게임

보드 각 칸에는 0~100 정수. 0은 빈칸, 100가지 다른 인형. 
moves 배열 크기는 1~1000
moves 배열 각 원소 값은 1 이상, 가로 크기 이하인 자연수
2차원 배열 N x N 정사각 격자. 위에는 크레인, 오른쪽에 바구니 (스택)
인형이 없으면 빈칸, 아래 칸부터 차곡차곡. 인형칸도 스택, 위에서부터
같은 모양 두 개가 바구니에서 연속으로 쌓이면 터짐-사라짐
인형 집어지지 않는 경우는 없고 인형 없는 곳에서 작동 시 아무 일도 없음
바구니는 충분히 크다. (NxN으로)
solution 함수 = 
매개변수: 2차원 배열 board, 크레인 작동시킨 위치가 담긴 배열 moves
리턴값: 크레인 모두 작동시킨 후 사라진 인형 개수

'''

def solution(board, moves):
    answer = 0
    bucket = []

    for i in moves:
      for j in range(len(board)):
        if board[j][i-1] != 0:
          bucket.append(board[j][i-1])
          board[j][i-1] = 0
      
          if len(bucket) > 1:
            if bucket[-1] == bucket[-2]:
              answer += 2
              bucket = bucket[:-2]
          break
          
    return answer
