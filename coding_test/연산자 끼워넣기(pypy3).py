max_num = float("-inf")
min_num = float("inf")

def calculate(num, operator):
    sum = num[0]
    for i in range(1, len(num)):
        if operator[i - 1] == 0:
            sum += num[i]
        elif operator[i - 1] == 1:
            sum -= num[i]
        elif operator[i - 1] == 2:
            sum *= num[i]
        elif operator[i - 1] == 3:
            temp = abs(sum) // num[i]
            if sum < 0:
                temp *= -1
            sum = temp            
    return sum

def back(num, operator, limit, selected, visited):
    global max_num, min_num
    if limit == 1:
        temp = calculate(num, selected)        
        min_num = min(min_num, temp)
        max_num = max(max_num, temp)
        return
    for i in range(len(operator)):
        if i in visited:
            continue
        selected.append(operator[i])
        visited.append(i)        
        back(num, operator, limit - 1, selected, visited)
        selected.pop()
        visited.pop()

def main():
    n = int(input())
    num = list(map(int, input().split()))
    sign = list(map(int, input().split()))
    operator = []
    for k in range(len(sign)):
        for i in range(sign[k]):
            operator.append(k)
    back(num, operator, n, [], [])
    print(max_num)
    print(min_num)

if __name__ == "__main__":
    main()