'''
https://www.acmicpc.net/problem/1541
백준 잃어버린 괄호 (실버2) - 그리디
'''
# 주어진 식에 괄호를 쳐서 이 값을 최소로 만들자. 

expression = input()

# -를 기준으로 나눈다. 
terms = expression.split('-')

result = sum(map(int, terms[0].split('+')))

for term in terms[1:]:
    result -= sum(map(int, term.split('+')))

print(result)