
def ransom_note(magazine, ransom,m,n):
    if m>=n:
        for k in ransom.keys():
            if k not in magazine.keys() or ransom[k]>magazine[k]:
                return False
        return True
    else: return False

m, n = map(int, input().strip().split(' '))
import collections
magazine = collections.Counter(input().strip().split(' '))
ransom = collections.Counter(input().strip().split(' '))
answer = ransom_note(magazine, ransom,m,n)
if(answer):
    print("Yes")
else:
    print("No")
    
