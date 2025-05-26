def fibo(n):
    if n == 0:
        return 0, 1, 0  # (fibo value, cnt_0, cnt_1)
    elif n == 1:
        return 1, 0, 1
    else:
        _, c0_1, c1_1 = fibo(n - 1)
        _, c0_2, c1_2 = fibo(n - 2)
        return c0_1 + c0_2, c0_1 + c0_2, c1_1 + c1_2  

T = int(input())

for _ in range(T):
    num = int(input())
    _, cnt_0, cnt_1 = fibo(num)
    print(cnt_0, cnt_1)

###########################################

cnt_0 = [0] * 41
cnt_1 = [0] * 41

cnt_0[0] = 1
cnt_1[1] = 1

for i in range(2, 41):
    cnt_0[i] = cnt_0[i - 1] + cnt_0[i - 2]
    cnt_1[i] = cnt_1[i - 1] + cnt_1[i - 2]

T = int(input())
for _ in range(T):
    num = int(input())
    print(cnt_0[num], cnt_1[num])
