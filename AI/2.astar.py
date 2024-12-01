import heapq

def heuristic(state, goal_state):
    h = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_position = next((r, c) for r, row in enumerate(goal_state) for c, v in enumerate(row) if v == value)
                h += abs(i - goal_position[0]) + abs(j - goal_position[1])
    return h

def is_goal(state, goal_state):
    return state == goal_state

def get_neighbors(state, parent_cost, goal_state):
    neighbors = []
    blank_row, blank_col = get_blank_position(state)

    for i, j, move in [(blank_row-1, blank_col, 'up'), (blank_row+1, blank_col, 'down'), 
                       (blank_row, blank_col-1, 'left'), (blank_row, blank_col+1, 'right')]:
        if 0 <= i < 3 and 0 <= j < 3:
            new_state = [row[:] for row in state]
            new_state[blank_row][blank_col], new_state[i][j] = new_state[i][j], new_state[blank_row][blank_col]
            action = f"Move {move}"
            cost = parent_cost + 1
            heuristic_value = heuristic(new_state, goal_state)
            neighbors.append((new_state, action, cost, heuristic_value))

    return neighbors

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def print_solution(solution):
    for step, (state, action, cost, heuristic_value) in enumerate(solution):
        print(f"Step {step}: {action}")
        print("\tCost:", cost)
        print("\tHeuristic value:", heuristic_value)
        print("\tState:")
        for row in state:
            print("\t", row)
        print("\n")

def a_star(initial_state, goal_state):
    heap = [(heuristic(initial_state, goal_state), 0, initial_state, [])]
    visited = set()

    while heap:
        _, cost, current_state, path = heapq.heappop(heap)

        if current_state == goal_state:
            print("Goal state reached!\n")
            solution = path + [(current_state, None, cost, 0)]  # Add the final state to the solution
            print_solution(solution)
            return

        visited.add(tuple(map(tuple, current_state)))

        for neighbor_state, action, neighbor_cost, heuristic_value in get_neighbors(current_state, cost, goal_state):
            if tuple(map(tuple, neighbor_state)) not in visited:
                heapq.heappush(heap, (heuristic_value + neighbor_cost, neighbor_cost, neighbor_state, path + [(current_state, action, neighbor_cost, heuristic_value)]))

    print("No solution found.")


initial_state = []
goal_state = []

print("Enter the initial state (3x3 matrix, use 0 for the blank space):")
for i in range(3):
    row = list(map(int, input().split()))
    initial_state.append(row)

print("\nEnter the goal state (3x3 matrix, use 0 for the blank space):")
for i in range(3):
    row = list(map(int, input().split()))
    goal_state.append(row)

print("\nSteps :-")
print("\n\tInitial State")
# for row in initial_state:
#     print('\t',row)

a_star(initial_state, goal_state)
