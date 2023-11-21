from collections import deque
class State:
    def __init__(self, missionaries, cannibals, boat, parent=None):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = parent
    def is_valid(self):
        return (self.missionaries >= 0 and self.cannibals >= 0 and
                3 - self.missionaries >= 0 and 3 - self.cannibals >= 0 and
                (self.missionaries == 0 or self.missionaries >= self.cannibals) and
                (3 - self.missionaries == 0 or 3 - self.missionaries >= 3 - self.cannibals))
    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0
    def successors(self):
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        if self.boat == 1:
            moves = [(-m, -c) for m, c in moves]
        for m, c in moves:
            new_state = State(self.missionaries + m, self.cannibals + c, 1 - self.boat, self)
            if new_state.is_valid():
                yield new_state
def print_solution(solution):
    path = []
    while solution:
        path.append((solution.missionaries, solution.cannibals, solution.boat))
        solution = solution.parent
    path.reverse()
    for state in path:
        print(state)
def breadth_first_search():
    initial_state = State(3, 3, 1)
    frontier = deque([initial_state])
    explored = set()
    while frontier:
        current_state = frontier.popleft()
        if current_state.is_goal():
            print("Solution found:")
            print_solution(current_state)
            return
        explored.add((current_state.missionaries, current_state.cannibals, current_state.boat))
        for child in current_state.successors():
            if (child.missionaries, child.cannibals, child.boat) not in explored:
                frontier.append(child)
    print("No solution found.")
breadth_first_search()
