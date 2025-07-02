# 2217 로프

N = int(input()) # N개의 로프

# k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량
# 이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량

ropes = [int(input()) for _ in range(N)]

ropes.sort(reverse=True)

max_weight = max(ropes[i] * (i + 1) for i in range(N))

max_weight = 0
for i in range(N):
    weight = ropes[i] * (i + 1)  # i+1개의 로프 사용
    max_weight = max(max_weight, weight)

print(max_weight)