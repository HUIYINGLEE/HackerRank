n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

def bubbleSort(a,n):
    numberOfSwaps=0
    for i in range(0, n):
        for j in range(0, n-1):
            if (a[j]>a[j+1]):
                aj=a[j]
                a[j]=a[j+1]
                a[j+1]=aj
                numberOfSwaps+=1
        if numberOfSwaps==0:
            break
    return numberOfSwaps
print("Array is sorted in",bubbleSort(a,n),"swaps." )
print("First Element:", a[0])
print("Last Element:", a[-1])

            
            
