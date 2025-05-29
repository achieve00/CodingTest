N = int(input())

n1, n2 = N // 10, N % 10
num = n2 * 10 + ((n1 + n2) % 10)

cycle = 1

while (num != N):
  n1, n2 = num // 10, num % 10
  num = n2 * 10 + ((n1 + n2) % 10)
  cycle += 1

print(cycle)