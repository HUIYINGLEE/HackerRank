def getBiggestRegion(grid,n,m):
    maxR=0
    for row in range(n):
        for col in range(m):
            maxR=max(maxR, count(grid,row,col,n,m))
    return maxR
def count(grib, row, col, n,m):
    if row in range(n) and col in range(m):
        if grid[row][col]==0:
            return 0
        else:
            c=1
            grid[row][col]=0
            c+=count(grib,row,col+1,n,m)
            c+=count(grib,row,col-1,n,m)
            c+=count(grib,row+1,col+1,n,m)
            c+=count(grib,row+1,col-1,n,m)
            c+=count(grib,row+1,col,n,m)
            c+=count(grib,row-1,col,n,m)
            c+=count(grib,row-1,col+1,n,m)
            c+=count(grib,row-1,col-1,n,m)
            return c
    else:return 0
    

n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid,n,m))
