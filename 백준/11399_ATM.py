# N명의 사람

# i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분

N = int(input())
P = list(map(int, input().split()))
result = 0
time = 0

P.sort()

for i in P:
  time += i
  result = result + time

print(result)