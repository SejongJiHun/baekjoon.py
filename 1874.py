import sys
input = sys.stdin.readline

n=int(input())
stack = []
result = []
cur = 1
status = 1
for i in range(n):
    x = int(input())
    while(cur <= x):
        stack.append(cur)
        result.append('+')
        cur += 1
    if (stack[-1] == x) :
        stack.pop()
        result.append('-')
    else:
        status = 0
        break

if status == 0:
    print("NO")
else:
    for item in result:
        print(item)

    
    



