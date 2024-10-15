'''
https://www.acmicpc.net/problem/13305
백준 주유소 (실버3)
''' 
n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))
total = 0
count = oil[0]

for i in range(n-1):
    if count > oil[i]:
        count = oil[i]
    total += count * road[i]
print(total)



# 17점
'''
for i  in range(n-1):
    if oil[i] == min(oil[i:n-1]):
        total += oil[i] * sum(road[i:])
        break
    else: 
        total += oil[i] * road[i]

print(total)
'''