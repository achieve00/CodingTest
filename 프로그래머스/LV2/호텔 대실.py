# 문제: 호텔 대실
# 플랫폼: 프로그래머스
# LV: 2
# 유형: 구현, 정렬, 시뮬레이션
# 난이도: 중
# 풀이 요약:
#   - 각 예약 시간을 분 단위로 변환하여 시작 시각 기준으로 정렬
#   - 예약이 끝나는 시간(청소 시간 포함)을 리스트에 저장하고,
#     현재 예약의 시작 시간보다 이전에 끝난 예약들을 booking 리스트에서 제거
#   - 동시에 사용 중인 방의 개수를 booking 리스트 길이로 판단하고, 최대값을 갱신
# 시간복잡도: O(n^2) — 예약마다 끝나는 방 리스트를 순회하며 필터링 (최대 n번 반복)


# H -> M으로 변경하는 함수
def hourToMin(times):
    start_H, start_M = times[0].split(':')
    end_H, end_M = times[1].split(':')
    start_H, start_M = int(start_H), int(start_M)
    end_H, end_M = int(end_H), int(end_M)
    
    start = start_H * 60 + start_M
    end = end_H * 60 + end_M + 10
    
    return start, end
    
def solution(book_time):
    answer = 0
    starts = [] # 시작 시간 모음
    ends = [] # 끝 시간 모음
    
    # 시작 시간을 기준으로 book_time 값을 정렬
    book_time.sort(key=lambda x: x[0])
    
    # 분 단위로 변환
    for times in book_time:
        start, end = hourToMin(times)
        starts.append(start)
        ends.append(end)

    booking = []  # 현재 사용 중인 방들의 종료 시간 리스트

    for i in range(len(starts)):
        start = starts[i]
        end = ends[i]

        # 이미 끝난 예약(b <= start) 들을 제거
        booking = [b for b in booking if b > start]

        # 현재 예약 추가
        booking.append(end)

        # 최대 방 개수 갱신
        answer = max(answer, len(booking))
            
    return answer


    ####################################################

# 유형: 구현, 정렬, 우선순위 큐(heap)
# 난이도: 중
# 풀이 요약:
#   - 예약 시간을 분 단위로 변환 후, 시작 시간 기준으로 정렬
#   - 각 예약에 대해 heap(우선순위 큐)을 사용해 현재 가장 빨리 비는 방의 종료 시간을 관리
#   - 시작 시간이 heap의 최소 종료 시간보다 크거나 같으면 해당 방 재사용 (pop), 아니면 새 방 추가
#   - heap에 남아 있는 방의 개수가 동시에 필요한 방의 최소 개수
# 시간복잡도: O(n log n) — 예약 정렬 O(n log n) + heap 삽입/삭제 O(log n)


import heapq

def hourToMin(times):
    start_H, start_M = map(int, times[0].split(':'))
    end_H, end_M = map(int, times[1].split(':'))

    start = start_H * 60 + start_M
    end = end_H * 60 + end_M + 10  # 퇴실 후 청소 시간 포함

    return start, end

def solution(book_time):
    # 예약 시간을 분 단위로 변환
    time_slots = [hourToMin(t) for t in book_time]

    # 시작 시간을 기준으로 정렬
    time_slots.sort(key=lambda x: x[0])

    rooms = []  # 종료 시간 저장용 min-heap

    for start, end in time_slots:
        # 현재 방 중 가장 빨리 끝나는 것보다 현재 예약 시작이 늦거나 같으면 그 방 재사용
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)
        heapq.heappush(rooms, end)  # 새 방 추가 or 재사용된 방 갱신

    return len(rooms)  # 남아있는 방 개수 = 최대 동시에 사용된 방 개수
