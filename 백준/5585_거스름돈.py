price = int(input())
charge = 1000 - price
coins = [500, 100, 50, 10, 5, 1]
cnt = 0

for coin in coins:
  if (charge // coin) > 0:
    plus = charge // coin
    charge = charge % coin
    cnt += plus
  
print(cnt)
