N, M = map(int, input().split())
# 맵 크기 N*M
x, y, direction = map(int, input().split())

game_map = []


for i in range(N):
  game_map.append(list(map(int, input().split())))

game_map[x][y] = 1
cnt = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 방향으로 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

# 회전해가면서 확인
turn_cnt = 0
while True:  
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  if game_map[nx][ny] == 0:
    game_map[nx][ny] = 1
    x = nx
    y = ny
    cnt += 1
    turn_cnt = 0
    continue
  else:
    turn_cnt += 1
  
  if turn_cnt == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    if game_map[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    turn_cnt = 0

print(cnt)