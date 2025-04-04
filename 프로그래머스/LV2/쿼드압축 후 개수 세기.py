# 문제: 쿼드압축 후 개수 세기
# 유형: 분할 정복, 재귀, 쿼드트리
# 난이도: 중
# 풀이 요약:
#   - 2차원 정사각 배열에서 0 또는 1로만 이루어진 값을 쿼드트리 방식으로 압축한다.
#   - 현재 영역이 모두 0이거나 1이면 해당 숫자의 개수를 1 증가시킨다.
#   - 모두 같지 않으면 4개의 사분면으로 나누어 재귀적으로 처리한다.
#   - 최종적으로 압축된 0과 1의 개수를 [0의 개수, 1의 개수] 형태로 반환한다.
# 시간복잡도: O(n^2) — 배열 전체를 최대 한 번씩 탐색하며, 재귀는 로그 레벨로 깊어짐


# 모두 1인지 확인하는 함수
def is_ones(arr, xl, yl, xr, yr):
    for i in range(xl, xr + 1):
        for j in range(yl, yr + 1):
            if arr[i][j] != 1:
                return False
    return True

# 모두 0인지 확인하는 함수
def is_zeroes(arr, xl, yl, xr, yr):
    for i in range(xl, xr + 1):
        for j in range(yl, yr + 1):
            if arr[i][j] != 0:
                return False
    return True

# 사각형 분할 및 개수 계산
def check_square(arr, xl, yl, xr, yr, result):
    if is_zeroes(arr, xl, yl, xr, yr):
        result[0] += 1
        return
    elif is_ones(arr, xl, yl, xr, yr):
        result[1] += 1
        return
    else:
        mid_x = (xl + xr) // 2
        mid_y = (yl + yr) // 2

        # 4분할로 재귀 호출
        check_square(arr, xl, yl, mid_x, mid_y, result)               # top-left
        check_square(arr, xl, mid_y + 1, mid_x, yr, result)           # top-right
        check_square(arr, mid_x + 1, yl, xr, mid_y, result)           # bottom-left
        check_square(arr, mid_x + 1, mid_y + 1, xr, yr, result)       # bottom-right


def solution(arr):
    answer = [0 ,0]
    n = len(arr)
    check_square(arr, 0, 0, n-1, n-1, answer)

    return answer