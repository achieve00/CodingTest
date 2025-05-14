M = int(input())
N = int(input())

total = 0
min_num = N

for num in range(M, N+1):
  if int(num ** 0.5) == (num ** 0.5):
    min_num = min(min_num, num)
    total += num

if total == 0: print(-1)
else:
    print(total)
    print(min_num)