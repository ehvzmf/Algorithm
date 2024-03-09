'''
https://www.acmicpc.net/problem/10799
백준 10799. 쇠막대기 (스택)

()레이저
(()) 쇠막대기가 겹쳐져 있고 몇 조각나는지
'''

answer = 0
razer = list(input())
st = []

for i in range(len(razer)):
    if razer[i] == '(':
        st.append('(')
    else:
        if razer[i-1] == '(':
            st.pop()
            answer += len(st)
        else:
            st.pop()
            answer += 1

print(answer)
