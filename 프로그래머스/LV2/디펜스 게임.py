from heapq import heappush, heappop

def solution(n, k, enemy):
    h = []
    for i, e in enumerate(enemy):
        heappush(h, e)
        if len(h) > k:
            n -= heappop(h)
        if n < 0:
            return i
            
    # 준호가 몇 라운드까지 막을 수 있는지 return
    return len(enemy)