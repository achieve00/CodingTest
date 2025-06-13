import pandas as pd
# 1205 등수 구하기

N, new_score, P = map(int, input().split())
# N: 리스트에 있는 점수 개수
# new_score: 태수의 새 점수
# P: 랭킹 리스트에 올라 갈 수 있는 점수의 개수
rank_list = []

if N > 0:
  rank_list = list(map(int, input().split()))
  # 리스트에 있는 점수 N (비오름차순)
  rank_list.sort(reverse=True)

# 랭킹 리스트에 올라가지 못할 경우
if (N >= P) and (rank_list[N-1] >= new_score):
  answer = -1
elif (N == 0):
  answer = 1
else:
  df = pd.DataFrame({'score':rank_list})
  df['rank'] = df['score'].rank(method='dense', ascending=False)
  higher = (df['score'] > new_score).sum()
  answer = higher + 1

print(answer)

#########################################################


N, new_score, P = map(int, input().split())

if N > 0:
    rank_list = list(map(int, input().split()))
else:
    rank_list = []

# 이미 꽉 차 있는 경우 먼저 확인
if N == P and N > 0 and rank_list[-1] >= new_score:
    print(-1)
else:
    rank_list.append(new_score)
    rank_list.sort(reverse=True)
    rank = rank_list.index(new_score) + 1

    if rank > P:
        print(-1)
    else:
        print(rank)


