from collections import deque

def gravity(arr, y, x, direction):
    N = len(arr)
    while 0 <= y < N and arr[y][x] == 0:
        y += direction
    y -= direction
    if y < 0 or y >= N:
        return -1, -1
    return y, x

def bfs(arr, start_y, start_x, target_y, target_x):
    N = len(arr)
    M = len(arr[0])
    directions = [(0, 1), (0, -1)]  # 오른쪽, 왼쪽
    queue = deque([(start_y, start_x, 1, 0)])  # (y, x, gravity_direction, flip_count)
    visited = [[[False, False] for _ in range(M)] for _ in range(N)]  # visited[y][x][gravity_direction]
    visited[start_y][start_x][1] = True

    while queue:
        y, x, gravity_direction, flip_count = queue.popleft()

        # 현재 중력 방향으로 이동
        new_y, new_x = gravity(arr, y, x, gravity_direction)
        if (new_y, new_x) == (target_y, target_x):
            return flip_count

        # 중력에 의해 더 이상 이동할 수 없으면 다음 상태로 진행
        for dy, dx in directions:
            ny, nx = new_y + dy, new_x + dx
            if 0 <= nx < M and arr[new_y][nx] == 0 and not visited[new_y][nx][gravity_direction]:
                visited[new_y][nx][gravity_direction] = True
                queue.append((new_y, nx, gravity_direction, flip_count))

        # 중력 방향을 뒤집기
        new_gravity_direction = -gravity_direction
        if not visited[new_y][new_x][new_gravity_direction]:
            visited[new_y][new_x][new_gravity_direction] = True
            queue.append((new_y, new_x, new_gravity_direction, flip_count + 1))

    return -1

def main():
    N, M = map(int, input().split())
    arr = []
    start_y, start_x, target_y, target_x = -1, -1, -1, -1
    for i in range(N):
        row = list(input().strip())
        arr.append([0 if ch == '.' else 1 if ch == '#' else 2 if ch == 'C' else 3 for ch in row])
        for j in range(M):
            if row[j] == 'C':
                start_y, start_x = i, j
            elif row[j] == 'D':
                target_y, target_x = i, j

    result = bfs(arr, start_y, start_x, target_y, target_x)
    print(result)

if __name__ == "__main__":
    main()
