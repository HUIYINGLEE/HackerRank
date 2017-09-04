def is_matched(expression):
    s=[]
    for exp in expression:
        if exp=='{':
            s.append('}')
        elif exp=='[':
            s.append(']')
        elif exp=='(':
            s.append(')')
        else:
            if len(s)==0 or exp!=s.pop():
                return False
    return len(s)==0

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
