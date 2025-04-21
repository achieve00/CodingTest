# 문제: 달리기 경주
# 플랫폼: 프로그래머스
# 레벨: 1
# 유형: 구현, 해시맵(딕셔너리) 최적화
# 풀이 요약:
#   - players: 현재 등수 순으로 정렬된 선수 이름 리스트
#   - callings: 불린 선수 이름 → 앞 선수와 순위 교체
#   - 선수 이름 → 현재 등수 딕셔너리(rank)를 유지하여 index() 대신 O(1) 조회
#   - 불릴 때마다 players 배열 내 위치 교환 + rank 딕셔너리 동기화
# 시간복잡도: O(m)

def solution(players, callings):
    rank = {name: i for i, name in enumerate(players)}
    
    for calling in callings:
        idx = rank[calling]
        players[idx], players[idx-1] = players[idx-1], players[idx]
        
        rank[players[idx]] = idx
        rank[players[idx - 1]] = idx - 1
        
    return players