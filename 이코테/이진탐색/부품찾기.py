# 문제: 부품 찾기
# 유형: 이진 탐색
# 난이도: 중
# 풀이 요약: 가게 보유 부품 리스트를 정렬한 후, 손님이 요청한 부품 번호를 이진 탐색으로 확인
# 시간복잡도: O(M * log N) – M: 요청 수, N: 가게 보유 부품 수

N = int(input()) # 가게의 총 부품 수
goods_list = list(map(int, input().split())) # 가게가 가지고 있는 부품 번호

M = int(input()) # 손님이 찾는 총 부품의 수
find_list = list(map(int, input().split())) # 손님이 찾는 부품 번호

# 이진 탐색 함수
def binary_search(array, target, start, end):
	if start > end: return None
	mid = (start + end) // 2
	if array[mid] == target: return mid
	elif array[mid] > target: return binary_search(array, target, start, mid -1)
	else:
		return binary_search(array, target, mid + 1, end)
  
# goods_list와 find_list 정렬
goods_list.sort()
find_list.sort()

for i in find_list:
  # find_list의 값을 순회
  result = binary_search(goods_list, i, 0, N-1)
  # 각 부품이 존재하면 yes, 아니면 no 출력
  if result != None: print('yes', end=' ')
  else:
    print('no', end=' ')