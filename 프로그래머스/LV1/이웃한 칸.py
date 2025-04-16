# 문제: 이웃한 칸칸
# 플랫폼: 프로그래머스
# 레벨: LV.1 
# 유형: 구현, 2차원 배열 탐색
# 풀이 요약:
#   - 주어진 좌표 (h, w)의 상하좌우에 인접한 네 칸을 검사
#   - 같은 색(문자)의 칸이 인접한 개수를 세어 반환
#   - 배열 인덱스가 범위를 벗어나지 않도록 조건을 설정
# 시간복잡도: O(1)
#   - 항상 상하좌우 4칸만 검사하므로 입력 크기와 무관


def solution(board, h, w):
    # 1. 정수를 저장할 변수 n을 만들고 board의 길이를 저장합니다.
    n = len(board)
    
    # 2. 같은 색으로 색칠된 칸의 개수를 저장할 변수 count를 만들고 0을 저장합니다.
    count = 0
    
    # 3. h와 w의 변화량을 저장할 정수 리스트 dh, dw를 만들고 각각 [0, 1, -1, 0], [1, 0, 0, -1]을 저장합니다.
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    # 4. 반복문을 이용해 i 값을 0부터 3까지 1 씩 증가시키며 아래 작업을 반복합니다.
    for i in range(4):
        # 4-1. 체크할 칸의 h, w 좌표를 나타내는 변수 h_check, w_check를 만들고 각각 h + dh[i], w + dw[i]를 저장합니다.
        h_check = h + dh[i]
        w_check = w + dw[i]
        # 4-2. h_check가 0 이상 n 미만이고 w_check가 0 이상 n 미만이라면 다음을 수행합니다.
        if h_check >= 0 and h_check < n and w_check >= 0 and w_check < n:
            # 4-2-a. board[h][w]와 board[h_check][w_check]의 값이 동일하다면 count의 값을 1 증가시킵니다.
            if board[h][w] == board[h_check][w_check]:
                count += 1
    
    # 5. count의 값을 return합니다.    
    return count