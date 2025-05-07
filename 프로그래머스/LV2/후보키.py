from itertools import combinations

def solution(relation):
    n_col = len(relation[0])
    n_row = len(relation)
    candidates = []

    # 모든 컬럼 조합을 부분 집합으로 생성
    for i in range(1, n_col + 1):
        for comb in combinations(range(n_col), i):
            # 현재 조합의 컬럼들로 만들어진 튜플들이 유일한지 검사
            projection = [tuple(row[col] for col in comb) for row in relation]
            if len(set(projection)) == n_row:
                # 최소성 검사: 이미 후보키로 인정된 것의 부분집합이면 제외
                if not any(set(c).issubset(set(comb)) for c in candidates):
                    candidates.append(comb)

    return len(candidates)
