N, M = map(int, input().split())
lpeople =[]
speople= []

for _ in range(N):
  person = input()
  lpeople.append(person)

for _ in range(M):
  person = input()
  speople.append(person)

union_people = list(set(lpeople) & set(speople))
union_people.sort()
print(len(union_people))
for people in union_people:
  print(people)