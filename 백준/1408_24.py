def time2sec(H, M, S):
  return H * 60 * 60 + M * 60 + S

def sec2time(S):
  sec = S % 60
  S = S // 60
  minute = S % 60
  hour = S // 60
  return hour, minute, sec

now_H, now_M, now_S = map(int, input().split(':'))
end_H, end_M, end_S = map(int, input().split(':'))

nowS = time2sec(now_H, now_M, now_S)
endS = time2sec(end_H, end_M, end_S)

S = (endS - nowS) % 86400

hour, minute, sec = sec2time(S)
formatted_time = f"{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(sec).zfill(2)}"

print(formatted_time)