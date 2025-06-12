from itertools import combinations

L, C = map(int, input().split())

# 암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다
# 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열
# 가능성 있는 암호들을 모두 구하는 프로그램을 작성

chars = input().split()
chars.sort()

# 모음 집합
vowels = {'a', 'e', 'i', 'o', 'u'}

# 조합으로 모든 경우 생성
for comb in combinations(chars, L):
    # 조건 필터링 (모음 ≥ 1, 자음 ≥ 2)
    vowel_count = sum(1 for ch in comb if ch in vowels)
    consonant_count = L - vowel_count

    if vowel_count >= 1 and consonant_count >= 2:
        print(''.join(comb))