# 문제: 숫자 카드 나누기 
# 플랫폼: 프로그래머스
# LV: 2
# 유형: 수학, 정수론, 최대공약수(GCD), 배열
# 난이도: 중
# 풀이 요약:
#   - 각각의 배열(arrayA, arrayB)의 모든 숫자들의 최대공약수(GCD)를 구한다.
#   - arrayA의 GCD로 arrayB의 모든 숫자를 나눌 수 없다면 → arrayA의 GCD는 유효한 후보
#   - 반대로 arrayB의 GCD로 arrayA의 모든 숫자를 나눌 수 없다면 → arrayB의 GCD도 후보
#   - 두 경우 중 더 큰 값을 반환
# 시간복잡도: O(n) — 배열 전체의 GCD를 구하는 데 O(n), 각 GCD 후보를 다른 배열과 비교하는 데 O(n)


from math import gcd
from functools import reduce

# 공약수 구하는 함수
def get_gcd(arr):
    return reduce(gcd, arr)

def solution(arrayA, arrayB):
    answer = 0

    gcdA = get_gcd(arrayA)
    gcdB = get_gcd(arrayB)

    # gcdA가 arrayB의 어떤 수로도 나눠지지 않아야 함
    if all(b % gcdA != 0 for b in arrayB):
        answer = max(answer, gcdA)

    # gcdB가 arrayA의 어떤 수로도 나눠지지 않아야 함
    if all(a % gcdB != 0 for a in arrayA):
        answer = max(answer, gcdB)

    return answer