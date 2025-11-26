import heapq

graph = {
    'Pune': [('Expressway', 50), ('oldHighway', 30), ('CoastalRoad', 20)],
    'Expressway': [('Mumbai', 100)],
    'oldHighway': [('Mumbai', 120)],
    'CoastalRoad': [('Mumbai', 180)],
    'Mumbai': []
}

heuristics = {
    'Pune': 150,
    'Expressway': 100,
    'oldHighway': 120,
    'CoastalRoad': 180,
    'Mumbai': 0
}

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

def a_star_search(start, goal):
    open_list = [] # (f_score, g_score, node_name)
    start_f = 0 + heuristics[start]
    heapq.heappush(open_list, (start_f, 0, start))

    came_from = {}
    g_score = {start: 0}
    closed_set = set()

    while open_list:
        current_g, current_f, current_node = heapq.heappop(open_list)

        if current_node == goal:
            return reconstruct_path(came_from, current_node)

        if current_node in closed_set:
            continue
        closed_set.add(current_node)

        if current_node in graph:
            for neighbor, movement_cost in graph[current_node]:
                temp_g = g_score[current_node] + movement_cost

                if neighbor not in g_score or temp_g < g_score[neighbor]:
                    came_from[neighbor] = current_node
                    g_score[neighbor] = temp_g

                    f_score = temp_g + heuristics[neighbor]
                    heapq.heappush(open_list, (f_score, temp_g, neighbor))
    return None

if __name__ == "__main__":
    start_node = 'Pune'
    goal_node = 'Mumbai'

    result_path = a_star_search(start_node, goal_node)
    print(f"Optimal Path: {result_path}")