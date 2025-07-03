import heapq
# 11000 강의실 배정

# Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능
# 수업이 끝난 직후에 다음 수업을 시작


N = int(input())

times = [list(map(int, input().split())) for _ in range(N)]
times.sort(key=lambda x: (x[0], x[1]))

heap = []
heapq.heappush(heap, times[0][1])  # 첫 수업의 종료 시간

for i in range(1, N):
    start, end = times[i]
    
    # 현재 수업 시작시간 >= 가장 빨리 끝나는 수업의 종료시간
    if start >= heap[0]:
        heapq.heappop(heap)  # 기존 강의실 사용 (종료 수업 제거)

    heapq.heappush(heap, end)  # 새 수업 넣기

print(len(heap))  # heap 크기 = 필요한 강의실 수