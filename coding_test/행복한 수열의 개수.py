n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

result = 0
for i in range(n):
    flag1 = False
    flag2 = False
    cnt1 = 1
    cnt2 = 1
    for j in range(n - 1):        
        if arr[i][j] != arr[i][j + 1]:
            if cnt1 >= m:
                flag1 = True
            cnt1 = 0
        if arr[j][i] != arr[j + 1][i]:
            if cnt2 >= m:
                flag2 = True
            cnt2 = 0
        cnt1 += 1
        cnt2 += 1
    if flag1 or cnt1 >= m:
        result += 1
    if flag2 or cnt2 >= m:
        result += 1
print(result)                    
    