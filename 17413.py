import sys
word=sys.stdin.readline().rstrip()

submit=[]

def reverse(w):
    stack=w.split()
    result = [ar[::-1] for ar in stack]
    return ' '.join(result)

while True:
    if word.find('<') == -1:
        submit.append(reverse(word))
        break
    else:
        first=word.find('<')
        end=word.find('>')
        
        part1=word[:first]
        if part1 : #빈문자열이 아니면 reverse 후 submit에 추가
            submit.append(reverse(part1))
        
        intact=word[first:end+1]#태그는 그대로 submit에 추가
        submit.append(intact)
        
        word=word[end+1:]#submit에 추가한거 제외
        
print(''.join(submit))
    
    
        
        
        
        