# https://www.acmicpc.net/problem/4673
# 백준 실버5 - 셀프 넘버 (브루트포스)

# d(n) = n + n의 각 자리 수, n은 d(n)의 생성자. 생성자가 없는 숫자는 셀프 넘버
# 10,000보다 작거나 같은 셀프 넘버 한 줄에 하나씩 출력

def self_num(n): # 생성자는 n, d(n) 반환하는 거 맞나? 
    x = list(str(n))
    result = 0
    for i in range(len(x)):
        result += int(x[i])
    result += n
    return result

results = set() # 중복 제거

for i in range(10000):
    results.add(self_num(i))
    
for m in range(1, 10001):
    if m not in results:
        print(m)