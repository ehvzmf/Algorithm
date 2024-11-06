'''
https://www.acmicpc.net/problem/18870
백준 좌표 압축 (실버2) - 정렬, 값/좌표 압축
key: 압축된 좌표는 index값
'''
n = int(input())
inputList = list(map(int, input().split()))

# 중복 제거 - set으로 만들고 다시 list로
sortedList = sorted(list(set(inputList)))
dictList = dict(zip(sortedList, list(range(len(sortedList)))))

for x in inputList:
    print(dictList[x])      