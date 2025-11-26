def is_valid(assignment, neighbors, color, regions):
    for neighbor in neighbors.get(regions, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def solve_csp(colors, regions, neighbors, assignment={}):
    if len(assignment) == len(regions):
        return assignment
    unassigned = [r for r in regions if r not in assignment][0]

    for color in colors:
        if is_valid(assignment, neighbors, color, unassigned):
            assignment[unassigned] = color
            result = solve_csp(colors, regions, neighbors, assignment)
            if result:
                return result
            del assignment[unassigned]
    return None

regions = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
colors = ['Red', 'Green', 'Blue']

neighbors = {
    'A' : ['B', 'C'],
    'B' : ['A', 'C', 'D'],
    'C' : ['A', 'B', 'D', 'E', 'F'],
    'D' : ['B', 'C', 'E'],
    'E' : ['D', 'F'],
    'F' : ['C', 'E'],
    'G' : []
}

solution = solve_csp(colors, regions, neighbors)
print(solution)