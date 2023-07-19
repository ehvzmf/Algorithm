'''

https://www.acmicpc.net/problem/10825
백준 10825번 - 국영수

도현이네 반 N명의 국영수 점수를 다음 조건으로 정렬:
  1. 국어 점수가 감소하는 순서
  2. 국어 점수가 같으면 영어 점수가 증가순
  3. 국=영 >> 수학 감소하는 순서로
  4. 모든 점수가 같으면 이름이 사전순으로 증가하는 순서로
  (단, 아스키코드에서 대문자는 소문자보다 작으므로 사전순으로 앞.)
INPUT : 첫째 줄에 반 학생 수 (1 <= N <= 100,000)
        둘째 줄부터 한 줄에 하나씩 각 학생의 이름, 국어, 영어, 수학 점수가 공백으로 구분해 주어짐
        (1 <= 점수 <= 100), 이름은 알파벳 대소문자 문자열, 길이는 10자리 미만
OUTPUT : 정렬 기준으로 N개의 줄에 걸쳐 학생 이름 출력

'''

N = int(input())
score = []

for i in range(N):
    [name, kor, eng, math] = map(str, input().split())
    score.append([name, int(kor), int(eng), int(math)])

sorted_score = sorted(score, key=lambda x : (-x[1], x[2], -x[3], x[0]))

for score in sorted_score:
    print(score[0])
