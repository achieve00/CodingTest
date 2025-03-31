# 문제: 상하좌우
# 유형: 구현, 시뮬레이션
# 난이도: 하
# 풀이 요약: 명령에 따라 위치를 이동시키되, 공간을 벗어나는 경우는 무시
# 시간복잡도: O(m) – m은 이동 명령 개수

# NXN 크기의 정사각형 공간에 서있음
# 가장 왼쪽 위 좌표 (1,1), 가장 아래 좌표(N,N)

L = [0, -1]
R = [0, 1]
U = [-1, 0]
D = [1, 0]

# 크기 밖을 벗어나면 명령 무시

N = int(input())
plans = input().split()
pos = [1, 1] # 시작 지점

for plan in plans:
  if pos[1] == 1 and plan == 'L': continue
  elif pos[1] == N and plan == 'R': continue
  elif pos[0] == 1 and plan == 'U': continue
  elif pos[0] == N and plan == 'D': continue
  
  if plan == 'L':
    pos[0] += L[0]
    pos[1] += L[1]
  elif plan == 'R':
    pos[0] += R[0]
    pos[1] += R[1]
  elif plan == 'U':
    pos[0] += U[0]
    pos[1] += U[1]
  elif plan == 'D':
    pos[0] += D[0]
    pos[1] += D[1]

print(pos)

# 방향별 이동 좌표
move = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

N = int(input())
plans = input().split()
pos = [1, 1]

for plan in plans:
    dx, dy = move[plan]
    nx = pos[0] + dx
    ny = pos[1] + dy
    if 1 <= nx <= N and 1 <= ny <= N:
        pos = [nx, ny]