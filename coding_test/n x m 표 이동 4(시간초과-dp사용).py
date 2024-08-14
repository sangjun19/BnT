# result = 0

# def dfs(y, x, n, arr, visited):
#     global result    
#     if y == len(arr) - 1 and x == len(arr[0]) - 1:
#         if n == 0:
#             result += 1
#         return
#     for dy, dx in [(1, 0), (0, 1)]:
#         ny, nx = y + dy, x + dx
#         if ny < 0 or ny >= len(arr) or nx < 0 or nx >= len(arr[0]):
#             continue
#         if arr[ny][nx] == 2:
#             continue
#         if (ny, nx) in visited:
#             continue
        
#         visited.append((ny, nx))
#         if arr[ny][nx] == 1:
#             dfs(ny, nx, n - 1, arr, visited)
#         else:
#             dfs(ny, nx, n, arr, visited)
#         visited.pop()

# def main():
#     n, m, a, b = map(int, input().split())
#     arr = [[0] * m for _ in range(n)]
#     for _ in range(a):
#         y, x = map(int, input().split())
#         arr[y - 1][x - 1] = 1
#     for _ in range(b):
#         y, x = map(int, input().split())
#         arr[y - 1][x - 1] = 2    
#     dfs(0, 0, a, arr, [(0, 0)])
#     print(result)
    
    
# if __name__ == "__main__":
#     main()

MOD = 1000000007

def count_paths(n, m, items, obstacles):
    # Initialize the grid with 0's
    dp = [[0] * m for _ in range(n)]
    
    # Mark obstacles in the grid
    obstacle_set = set(obstacles)
    
    # Mark items in the grid and store their positions
    item_positions = sorted(items)
    
    # Starting point
    dp[0][0] = 1 if (1, 1) not in obstacle_set else 0
    
    # Fill the dp array
    for x, y in item_positions + [(n, m)]:
        new_dp = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if (i + 1, j + 1) in obstacle_set:
                    continue
                if i > 0:
                    new_dp[i][j] = (new_dp[i][j] + dp[i - 1][j]) % MOD
                if j > 0:
                    new_dp[i][j] = (new_dp[i][j] + dp[i][j - 1]) % MOD
        
        dp = new_dp
    
    return dp[n - 1][m - 1]

# 입력
n, m, a, b = map(int, input().split())
items = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(a)]
obstacles = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(b)]

# 결과 계산 및 출력
result = count_paths(n, m, items, obstacles)
print(result)
