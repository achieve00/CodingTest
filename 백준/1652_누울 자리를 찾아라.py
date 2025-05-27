import re

N = int(input())
room = []

for _ in range(N):
    room.append(input())

c, r = 0, 0

# 가로
for line in room:
    c += len(re.findall(r'\.{2,}', line))

# 세로
room_T = [''.join(row[i] for row in room) for i in range(N)]
for line in room_T:
    r += len(re.findall(r'\.{2,}', line))

print(c, r)
