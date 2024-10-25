'''
https://www.acmicpc.net/problem/18870
백준 좌표 압축 (실버2) - 정렬, 값/좌표 압축
'''
'''
n = int(input())
arr = list(map(int, input().split()))
'''
import sys

N = int(input())
inputList = list(map(int,sys.stdin.readline().rstrip().split()))

sortedList = sorted(list(set(inputList)))
dictList = dict(zip(sortedList,list(range(len(sortedList)))))

for x in inputList:
    print(dictList[x])