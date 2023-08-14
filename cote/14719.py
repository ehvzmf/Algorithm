'''
https://www.acmicpc.net/problem/14719
백준 14719 - 빗물 (구현, 시뮬레이션)
'''

h, w = map(int, input().split())
world = list(map(int, input().split()))

ans = 0
for i in range(1, w-1):
    l_max = max(world[:i])
    r_max = max(world[i+1:])
    
    compare = min(l_max, r_max)
    
    if world[i] < compare:
        ans += compare - world[i]
        
print(ans)
