def solve(maze):
    n = len(maze)
    if n == 0 or maze[0][0] == 0:
        return []

    dirs = [('D', 1, 0), ('U', -1, 0), ('R', 0, 1), ('L', 0, -1)]
    visited = [[False] * n for _ in range(n)]
    results = []
    path = []

    def df(r, c):
        if r == n - 1 and c == n - 1:
            results.append(''.join(path))
            return

        for move, dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and maze[nr][nc] == 1:
                visited[nr][nc] = True
                path.append(move)
                df(nr, nc)
                path.pop()
                visited[nr][nc] = False

    visited[0][0] = True
    df(0, 0)
    return results


# Example
maze = [
    [1, 0, 0, 0],
    [1, 1, 1, 0],
    [1, 1, 0, 1],
    [0, 1, 1, 1]
]
print(solve(maze))
