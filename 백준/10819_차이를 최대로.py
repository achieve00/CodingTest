from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))

max_sum = 0

for perm in permutations(nums):
    curr_sum = sum(abs(perm[i] - perm[i+1]) for i in range(N-1))
    max_sum = max(max_sum, curr_sum)

print(max_sum)