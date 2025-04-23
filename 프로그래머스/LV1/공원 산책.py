# 문제: 공원 산책
# 플랫폼: 프로그래머스
# 레벨: 1
# 유형: 구현, 시뮬레이션
# 풀이 요약:
#   - 2차원 공원 지도에서 'S'는 시작 위치, 'X'는 장애물
#   - routes 리스트에 주어진 방향/횟수만큼 이동 가능한지 시뮬레이션
#   - 이동 경로 중 하나라도 장애물 또는 공원 밖이면 해당 명령은 무시
#   - 모든 명령을 시뮬레이션한 뒤, 최종 위치 반환
# 시간복잡도: O(n * k)

def solution(park, routes):
    
    w = len(park[0])
    h = len(park)
    
    # 동서남북
    dirs = {
    'N': [-1, 0],
    'E':[0, 1],
    'S': [1, 0],
    'W': [0, -1]
    }
    
    # park를 split
    park = [list(row) for row in park]
    
    # 시작 위치
    for i in range(len(park)):
        if 'S' in park[i]:
            pos = [i, park[i].index('S')]
            break

    
    for route in routes:
        # d: 방향, cnt: 이동 칸수
        d, cnt = route.split()
        cnt = int(cnt)
        valid = True
        
        # 다음 step
        for step in range(1, cnt + 1):
            ny = pos[0] + dirs[d][0] * step
            nx = pos[1] + dirs[d][1] * step

            if not (0 <= ny < h and 0 <= nx < w):
                valid = False
                break
            if park[ny][nx] == 'X':
                valid = False
                break

        if valid:
            pos = [pos[0] + dirs[d][0] * cnt, pos[1] + dirs[d][1] * cnt]
    
    return pos