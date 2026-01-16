# 몫 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120805
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 01. 16. 22:40:13

def solution(num1, num2):
    if 0<=num1<=100 and 0<=num2<= 100:
        answer = int(num1 /num2)
        return answer