# 문제: 방금그곡
# 플랫폼: 프로그래머스
# LV: 2
# 유형: 구현, 문자열 처리, 정규표현식
# 난이도: 중
# 풀이 요약:
#   - 멜로디에 포함된 샾음(C# 등)을 일반 알파벳으로 치환해 비교의 정확도를 높인다.
#   - 음악의 재생 시간을 계산하고, 해당 시간 동안 멜로디를 반복 생성한다.
#   - 기억한 멜로디(m)가 반복된 전체 멜로디에 포함되는지 확인한다.
#   - 조건을 만족하는 음악 중 가장 재생 시간이 긴 곡을 고르고, 동일할 경우 먼저 입력된 곡을 선택한다.
# 시간복잡도: O(n * L) — n: 음악의 개수, L: 최대 재생된 멜로디 길이


import re

def convert_melody(m, convert_dict):
    for sharp_note, replacement in convert_dict.items():
        m = m.replace(sharp_note, replacement)
    return m

# H -> M으로 변경하는 함수
def hourToMin(start_time, end_time):
    start_H, start_M = start_time.split(':')
    end_H, end_M = end_time.split(':')
    start_H, start_M = int(start_H), int(start_M)
    end_H, end_M = int(end_H), int(end_M)
    
    start = start_H * 60 + start_M
    end = end_H * 60 + end_M
    
    return start, end

def solution(m, musicinfos):
    
    #네오가 기억한 멜로디와 악보에 사용되는 
    convert_dict = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a', 'B#': 'b', 'E#': 'e'}
    m = convert_melody(m, convert_dict)
    pattern = r""+ re.escape(m)
    infos = []
    
    
    for idx, music in enumerate(musicinfos):
        start_time, end_time, title, melody = music.split(',')
        start, end = hourToMin(start_time, end_time)
        music_len = end - start
        
        melody = convert_melody(melody, convert_dict)
        melody = melody * (music_len // len(melody)) + melody[:music_len % len(melody)]
        
        if re.search(pattern, melody):
            infos.append([title, music_len, True, idx])
        
    filtered = [info for info in infos if info[2]]

    if filtered:
        longest = max(filtered, key=lambda x: (x[1], -x[3]))
        return longest[0]
    else:
        return "(None)"
    