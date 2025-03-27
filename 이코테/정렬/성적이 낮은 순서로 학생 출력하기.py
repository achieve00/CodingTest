n = int(input())
array = []

for i in range(n):
  input_data = input().split()
  name = input_data[0]
  grade = int(input_data[1])
  
  array.append((name, grade))

array = sorted(array, key=lambda x: x[1])

for i in array:
  print(i[0], end=' ')