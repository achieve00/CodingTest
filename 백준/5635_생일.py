n = int(input()) # n은 학생 수

students = []

for i in range(n):
  name, d, m, y = input().split()
  d, m, y = int(d), int(m), int(y)
  student = [name, y, m, d]
  students.append(student)

students.sort(key=lambda x: (x[1], x[2], x[3])) 

print(students[-1][0])
print(students[0][0])
