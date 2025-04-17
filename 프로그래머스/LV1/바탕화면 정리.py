# 문제: 바탕화면 정리
# 플랫폼: 프로그래머스
# 레벨: 1
# 유형: 구현, 시뮬레이션
# 풀이 요약:
#   - wallpaper는 문자열 2차원 배열로, '#'는 파일이 있는 위치를 의미
#   - 모든 '#'의 좌표 중 가장 왼쪽 위와 오른쪽 아래 경계를 찾아 드래그 영역을 지정
#   - 좌상단 (row_min, col_min), 우하단 (row_max+1, col_max+1)을 리스트로 반환
#   - 드래그는 직사각형이므로 최소 행/열 ~ 최대 행/열까지 포함되도록 함
# 시간복잡도: O(n * m)


def solution(wallpaper):
    
    row_min, col_min = float('inf'), float('inf')
    row_max, col_max = -1, -1

    for i, row in enumerate(wallpaper):
        for j, cell in enumerate(row):
            if cell == '#':
                row_min = min(row_min, i)
                col_min = min(col_min, j)
                row_max = max(row_max, i)
                col_max = max(col_max, j)
    
    return [row_min,col_min,row_max+1,col_max+1]