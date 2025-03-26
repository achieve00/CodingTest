# 시작 지점
input_pos = input()
# 8*8 평면이므로 갈 수 있는 최대한의 위치
max_pos = 8

chese_col = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8
}
row = int(input_pos[1])
col = chese_col[input_pos[0]]

cnt = 0

# 방향별 이동 좌표
moves = [(-2, -1),(-2, 1),(2, -1),(2, 1), (-1, -2),(-1, 2),(1, -2),(1, 2)]

for move in moves:
  nx = row + move[0]
  ny = col + move[1]
  if nx <= 1 or ny <= 1 or nx >= max_pos or ny >= max_pos:
    continue
  cnt += 1

print(cnt)