def solution(players, m, k):
    answer = 0
    expire = [0] * (len(players) + k)
    capacity = m

    for t, user in enumerate(players):
        capacity -= expire[t] * m

        if capacity <= user:
            add = (user - capacity) // m + 1
            answer += add
            capacity += add * m
            expire[t + k] += add

    return answer
