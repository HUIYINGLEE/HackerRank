def count_inversions(a):
    count=0
    if len(a)>1:
        mid=len(a)//2
        left=a[:mid]
        right=a[mid:]
        count+=count_inversions(left)
        count+=count_inversions(right)
        
        l=0
        r=0
        aIndex=0
        swaps=0
        while l<len(left) and r<len(right):
            if left[l]>right[r]:
                a[aIndex]=right[r]
                r+=1
                swaps+=mid-l
            else:
                a[aIndex]=left[l]
                l+=1
            aIndex+=1
        while l<len(left):
            a[aIndex]=left[l]
            l+=1
            aIndex+=1
        while r<len(right):
            a[aIndex]=right[r]
            r+=1
            aIndex+=1
        count+=swaps
    return count
      

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    print count_inversions(arr)
