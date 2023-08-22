def bubble_sort(s, e, n):
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            # 끝나는 시간이 같은 경우는 시작 시간이 더 빠른 순으로 정렬
            if e[j] > e[j+1] or e[j] == e[j+1] and s[j] > s[j+1]:
                tmp = s[j]
                s[j] = s[j+1]
                s[j+1] = tmp
                tmp = e[j]
                e[j] = e[j+1]
                e[j+1] = tmp

def solution(s, e, n):
    answer = 0
    e1 = e2 = -1

    bubble_sort(s, e, n)

    for now_s,now_e in zip(s,e):
        if e1 <= now_s:
            answer += 1
            e1 = now_e
        elif e2 <= now_s:
            e2 = e1
            e1 = now_e
            answer+=1

    return answer


if __name__ == '__main__':
    n = int(input())
    s = list(map(int,input().split(" ")))
    e = list(map(int,input().split(" ")))
    answer = solution(s, e, n)
    print(answer)
