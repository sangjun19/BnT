n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

result = 0
def straight(gy, gx, count, sum, dir):
    global arr
    if count == 0:
        return gy, gx, sum
    if dir == 0:
        return straight(gy - 1, gx + 1, count - 1, sum + arr[gy][gx], dir)
    elif dir == 1:
        return straight(gy - 1, gx - 1, count - 1, sum + arr[gy][gx], dir)
    elif dir == 2:
        return straight(gy + 1, gx - 1, count - 1, sum + arr[gy][gx], dir)
    elif dir == 3:
        return straight(gy + 1, gx + 1, count - 1, sum + arr[gy][gx], dir)
    
result = 0
for i in range(n):
    for j in range(n):                    
        if j == 0 or j == n - 1 or i <= 1:
            continue
        sum = 0
        ya, xa = i, j        
        for a in range(1, n - 1):
            if ya - a < 0 or xa + a > n - 1: continue            
            yb, xb, suma = straight(ya, xa, a, sum, 0)            
            for b in range(1, n - 1):
                if yb - b < 0 or xb - b < 0: continue                
                yc, xc, sumb = straight(yb, xb, b, suma, 1)
                for c in range(1, n - 1):
                    if yc + c > n - 1 or xc - c < 0: continue
                    yd, xd, sumc = straight(yc, xc, c, sumb, 2)
                    for d in range(1, n - 1):
                        if yd + d > n - 1 or xd + d > n - 1: continue
                        y, x, sumd = straight(yd, xd, d, sumc, 3)
                        if y == i and x == j:
                            result = max(result, sumd)
print(result)
