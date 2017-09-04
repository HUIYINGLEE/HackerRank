def iceCream(menue, money):
    dic={}
    for ID, price in enumerate(menue, 1):
        if money-price in dic:
            return dic[money-price],ID
        dic[price]=ID
    return None
                    
    
        
            
        
               
import bisect 
t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    first, second= iceCream(a,m)
    print(first, second)
    
    
