# 1트 : 2차원 배열 - n * 가장 높은 높이

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

# 2트 : 2차원 배열 - 각 행높이 만큼

# n = int(input())
# arr = []
# for _ in range(n):
#     value = int(input())
#     arr.append([i for i in range(1, value + 1)])

# max_num = float("-inf")

# for i in range(1, n):
#     for j in range(len(arr[i])):        
#         if len(arr[i - 1]) < j + 1:
#             continue
#         arr[i][j] += arr[i - 1][j]
#         max_num = max(max_num, arr[i][j])

# # for a in arr:
# #     print(*a)

# print(max_num)

# 3트 : 1차원 배열로, 2차원 for문(시간초과)

# n = int(input())
# arr = []
# arr2 = set()
# max_num = float("-inf")
# for i in range(n):
#     arr.append(int(input()))
#     arr2.add(arr[i])
#     max_num = max(max_num, arr[i])

# result = 0
# for k in arr2:
#     pos, cnt, result = -1, 0, result
#     for i in range(n):
#         if arr[i] < k:
#             continue
#         if pos == -1:
#             pos = i
#             cnt = 1
#         else:
#             if i - pos == 1:     
#                 pos = i           
#                 cnt += 1
#     result = max(result, cnt * k)
# result = max(result, n)
# print(result)

# 4트 : stack이용

n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))
arr.append(0)
stack = [0]
result = 0

for i in range(1, n + 2):    
    while stack and arr[stack[-1]] > arr[i]:
        height = arr[stack.pop()]
        width = i - stack[-1] - 1
        result = max(result, height * width)
    stack.append(i)
print(result)