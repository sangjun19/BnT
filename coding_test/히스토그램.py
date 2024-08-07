# n = int(input())
# arr = [0]
# for _ in range(n):
#     arr.append(int(input()))
# result = [[0 for _ in range(n + 1)] for _ in range(max(arr) + 1)]

# max_num = float("-inf")
# result [1][1] = 1
# for i in range(1, len(result)):
#     for j in range(1, n + 1):
#         if i > arr[j]:
#             continue
#         result[i][j] = (i + result[i][j - 1])
#         max_num = max(max_num, result[i][j])

# # for r in result:
# #     print(*r)

# print(max_num)

n = int(input())
arr = []
for _ in range(n):
    value = int(input())
    arr.append([i for i in range(1, value + 1)])

max_num = float("-inf")

for i in range(1, n):
    for j in range(len(arr[i])):        
        if len(arr[i - 1]) < j + 1:
            continue
        arr[i][j] += arr[i - 1][j]
        max_num = max(max_num, arr[i][j])

for a in arr:
    print(*a)

# print(max_num)