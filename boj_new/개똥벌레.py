'''
https://www.acmicpc.net/problem/3020
백준 개똥벌레 (골드5) - 이분탐색/누적합
python 제출 시 시간초과 (pypy로 제출)
'''

# 값 처음 나타나는 위치
def lower_bound(arr, target):
    start, end = 0, len(arr)
    
    while start < end:
        mid = (start + end) // 2

        if target <= arr[mid]:
            end = mid
        else:
            start = mid + 1
    
    return start

n, h = map(int, input().split())
tites,mites = [], []
for _ in range(n // 2):
    tites.append(int(input())) # 석순
    mites.append(int(input())) # 종유석
tites.sort()
mites.sort()
obs_cnt = [0] * h

for i in range(h):
    obs_cnt[i] = n // 2 - lower_bound(tites, i + 1) + n // 2 - lower_bound(mites, h - i)
    # 석순의 총 개수 - lower_bound (정렬되어 있기 떄문에)
    # 종유석은 반대 (거꾸로 붙어 있으니까) 

print(min(obs_cnt), obs_cnt.count(min(obs_cnt)))