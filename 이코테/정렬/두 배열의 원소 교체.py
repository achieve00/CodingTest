# 문제: 두 배열의 원소 교체
# 유형: 정렬, 그리디
# 난이도: 중
# 풀이 요약: 가장 작은 A와 가장 큰 B를 최대 K번 교환 (A의 합 최대화), 더 이상 교환할 필요가 없으면 중단
# 시간복잡도: O(n log n) – 정렬 2번

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else: break

print(sum(a))