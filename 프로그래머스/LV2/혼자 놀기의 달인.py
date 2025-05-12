def solution(cards):
    visited = [False] * len(cards) # 방문 여부
    sizes = []

    for i in range(len(cards)):
        if not visited[i]:
            count = 0
            idx = i
            while not visited[idx]:
                visited[idx] = True
                idx = cards[idx] - 1
                count += 1
            sizes.append(count)
        
    sizes.sort(reverse=True)

    if len(sizes) >= 2:
        return sizes[0] * sizes[1]
    else:
        return 0