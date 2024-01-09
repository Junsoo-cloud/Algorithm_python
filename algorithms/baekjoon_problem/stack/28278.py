import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
n = int(input())

stack = list()

for _ in range(n):
    command = input().rstrip()
    print(f'command -> {command}')
    print(f'len -> {len(command)}')
    if len(command) >= 2:
        stack.append(int(command[2:]))
    elif command == "2":
        if stack:
            tmp = stack.pop()
            print(tmp)
        else:
            print(-1)
    elif command == "3":
        print(len(stack))
    elif command == "4":
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)