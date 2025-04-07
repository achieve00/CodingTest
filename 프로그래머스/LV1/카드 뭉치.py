# 문제: 카드뭉치
# 유형: 구현, 포인터
# 풀이 요약: 
# 1. goal의 각 단어를 순서대로 확인하며, cards1 또는 cards2에서 해당 단어를 순서대로 꺼낼 수 있는지 확인
# 2. 각 카드 뭉치에 포인터(i, j)를 두고, 현재 단어가 cards1[i] 또는 cards2[j]와 같으면 포인터를 이동
# 3. 둘 다 아니라면 순서를 맞출 수 없으므로 "No" 반환
# 시간복잡도: O(n)

def solution(cards1, cards2, goal):
    i = 0 # cards1
    j = 0 # cards2
    
    for word in goal:
        if (i < len(cards1)) and (word == cards1[i]):
            i += 1
        else:
            if (j < len(cards2)) and (word == cards2[j]):
                j += 1
            else:
                return "No"
            
    return "Yes"