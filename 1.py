from collections import deque

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def get_neighbors(state):
    neighbors = []
    idx = state.index(0) #find the position of empty tile
    r, c = divmod(idx, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr <3 and 0 <= nc <3:
            new_idx = nr * 3 + nc
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(tuple(new_state))
    return neighbors

def bfs_solve(start_state):
    if start_state == GOAL:
        return [start_state]

    queue = deque([(start_state, [])])
    visited = set([start_state])

    while queue:
        current, path = queue.popleft()
        if current == GOAL:
            return path + [current]

        for neighbors in get_neighbors(current):
            if neighbors not in visited:
                visited.add(neighbors)
                queue.append((neighbors, path + [current]))
    return None

def dfs_solve(start_state):
    if start_state == GOAL:
        return [start_state]
    
    stack = [(start_state, [])]
    visited = set([start_state])

    while stack:
        current, path = stack.pop()

        if current == GOAL:
            return path + [current]

        for neighbors in get_neighbors(current):
            if neighbors not in visited:
                visited.add(neighbors)
                stack.append((neighbors, path + [current]))
    return None

start = (1, 2, 3, 4, 5, 6, 7, 0, 8)

bfs_result = bfs_solve(start)
print(bfs_result)

dfs_result = dfs_solve(start)
print(dfs_result)

    
