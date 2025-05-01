import re
from itertools import permutations

# 연산 함수
def calc(a, b, op):
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b

# 계산
def evaluate(nums, ops, priority):
    nums = nums[:]
    ops = ops[:]
    
    # 우선순위부터 계산
    for op in priority:
        idx = 0
        while idx < len(ops):
            if ops[idx] == op:
                result = calc(nums[idx], nums[idx + 1], op) 
                # 연산 결과로 교체
                nums[idx] = result
                del nums[idx + 1] # 오른쪽 피연산자 제거
                del ops[idx] # 해당 연산자 제거
            else:
                idx += 1
    # 절대값
    return abs(nums[0])
    
def solution(expression):
    answer = 0
    
    # 참가자의 미션은 전달받은 수식에 포함된 연산자의 우선순위를 자유롭게 재정의하여 만들 수 있는 가장 큰 숫자를 제출
    priorities = list(permutations(['*', '+', '-']))
    
    # expression의 숫자 추출
    numbers = list(map(int, re.findall(r'\d+', expression)))
    operaters = re.findall(r'[\+\-\*]', expression)
    
    results = []
    
    for p in priorities:
        result = evaluate(numbers, operaters, p)
        results.append(result)
    
    answer = max(results)
    return answer