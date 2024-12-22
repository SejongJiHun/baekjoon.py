import sys
input = input = sys.stdin.readline

def check_vps(ps)
    stack = []
    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack :
                return "NO"
            else:
                stack.pop()
    if not stack :
        return "YES"
    else:
        return "NO"
                

n=int(input())
results = []
for i in range(n):
    arr = list(input())
    results.append(check_vps(arr))
    print(results[i])
    
    