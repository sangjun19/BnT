# 50점 - 실패

s = input()
q = int(input())
arr = []
for _ in range(q):
    arr.append(input().split(" "))

for i in range(q):
    cnt = 0
    for k in range(int(arr[i][1]), int(arr[i][2]) + 1):
        if s[k] == arr[i][0]:
            cnt += 1
    print(cnt)
