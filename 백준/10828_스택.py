N = int(input())
stack = []

for _ in range(N):
  command = input()
  if 'push' in command:
      _, num = command.split()
      stack.append(int(num))

  elif command == 'pop':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack.pop())
  
  elif command == 'size':
    print(len(stack))
  
  elif command == 'empty':
    print(1 if len(stack) == 0 else 0)

  elif command == 'top':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])
      