n = int(input())
arr = []
position = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            continue
        position.append((i, j))

result = [] # 점수를 저장할 리스트
limit = len(position) # 폭탄을 놓을 수 있는 위치의 개수

def calculate(num):
    global n, position
    check = set()
    for l in range(len(position)):
        i, j = position[l]
        k = num[l]

        check.add((i, j))
        if k == 0:
            check.add((i - 1, j))
            check.add((i - 2, j))
            check.add((i + 1, j))
            check.add((i + 2, j))
        elif k == 1:
            check.add((i, j - 1))
            check.add((i, j + 1))
            check.add((i - 1, j))
            check.add((i + 1, j))
        else:
            check.add((i - 1, j - 1))
            check.add((i - 1, j + 1))
            check.add((i + 1, j - 1))
            check.add((i + 1, j + 1))

    check = {(x, y) for x, y in check if x >= 0 and y < n and x < n and y >= 0}
    # print(check, num, len(check))
    return len(check)

def find(num, cnt) :
    global limit, result
    if cnt == limit:
        result.append(calculate(num))
        return
    for k in range(3):
        num.append(k)
        find(num, cnt + 1)
        num.pop()
    return        

find([], 0)
print(max(result)) # 최대값 출력