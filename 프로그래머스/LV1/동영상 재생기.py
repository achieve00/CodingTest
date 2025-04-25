def minToSec(time):
    M, S = map(int, time.split(':'))
    return M * 60 + S

def secToMin(time):
    return f"{time // 60:02d}:{time % 60:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    video_len = minToSec(video_len)
    pos = minToSec(pos)
    op_start = minToSec(op_start)
    op_end = minToSec(op_end)

    for command in commands:
        if op_start <= pos <= op_end:
            pos = op_end

        if command == 'prev':
            pos = max(0, pos - 10)
        elif command == 'next':
            pos = min(video_len, pos + 10)
        
        if op_start <= pos <= op_end:
            pos = op_end

    return secToMin(pos)