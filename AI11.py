def is_valid_assignment(assignment, node, color):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True
def backtracking(assignment):
    if len(assignment) == len(graph):
        return assignment
    node = select_unassigned_variable(assignment)
    for color in colors:
        if is_valid_assignment(assignment, node, color):
            assignment[node] = color
            result = backtracking(assignment)
            if result is not None:
                return result
            del assignment[node]
    return None
def select_unassigned_variable(assignment):
    for node in graph:
        if node not in assignment:
            return node
colors = ['Red', 'Green', 'Blue']
graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW']
}
assignment = backtracking({})
if assignment is not None:
    print("Map Coloring Solution:")
    for node, color in assignment.items():
        print(f"{node}: {color}")
else:
    print("No solution found.")
