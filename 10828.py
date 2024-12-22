import sys
input = sys.stdin.readline

n = int(input(()
stack = []

for i in range(n):
    cmd = input().split()
    if(cmd[0] == "push"):
        stack.append(int(cmd[1]))

    elif(cmd[0] == "pop"):
        if(len(stack) >= 1):
            removed = stack.pop()
            print(removed)
        else:
            print(-1)

    elif(cmd[0] == "size"):
        print(len(stack))

    elif(cmd[0] == "empty"):
        if(len(stack) == 0):
            print(1)
        else:
            print(0)

    elif(cmd[0] == "top"):
        if(len(stack) >= 1):
            print(stack[-1])
        else:
            print(-1)
        





