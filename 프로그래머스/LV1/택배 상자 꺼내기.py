def solution(n, w, num):
    # 층 수 계산
    h = (n + w - 1) // w
    board = [[None] * w for _ in range(h)]
    count = 1
    pos_row = pos_col = 0

    # 창고에 상자 쌓기 (지그재그)
    for i in range(h):
        rng = range(w) if i % 2 == 0 else range(w-1, -1, -1)
        for j in rng:
            if count > n:
                break
            board[i][j] = count
            if count == num:
                pos_row, pos_col = i, j
            count += 1

    # num 위에 있는 상자 개수 세기
    answer = 1  # 자기자신 포함
    for row in range(pos_row + 1, h):
        if board[row][pos_col] is not None:
            answer += 1

    return answer
