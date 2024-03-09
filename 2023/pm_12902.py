'''
https://school.programmers.co.kr/learn/courses/30/lessons/12902
프로그래머스 3 X n 타일링 (12902)
가로 2 세로 1 직사각형 타일로 세로 3 가로 n인 바닥 채우기. 가로/세로로 배치 가능
solution 함수 - 가로 길이 n이 매개변수로 주어질 때 채우는 방법의 수를 리턴
(가로 길이 n <= 5,000)
(경우의 수가 많아질 수 있으므로 경우의 수를 1,000,000,007)로 나눈 나머지를 return)
'''
def solution(n):
    if n % 2:
        return 0
    front = back = 1
    for _ in range(n//2):
        front, back = back, (4*back - front) % 1000000007
    return back
