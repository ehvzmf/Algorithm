'''
https://www.acmicpc.net/problem/1253
백준 좋다 (골드4) - 이분 탐색, 투 포인터
Hint: 3,4,5,6,7,8,9,10은 좋다.
'''
# N개의 수 중 어떤 수가 다른 수 두개의 합으로 나타낼 수 있으면 좋다(GOOD)
# 좋은 수는 몇 개인지 출력
# 수의 위치가 다르면 값이 같아도 다른 수. 

n = int(input())
A = list(map(int, input().split()))

