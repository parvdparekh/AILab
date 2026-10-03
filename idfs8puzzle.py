# Adjacency moves for the 3x3 grid
MOVES = [
    [1, 3],       [0, 2, 4],    [1, 5],
    [0, 4, 6],    [1, 3, 5, 7], [2, 4, 8],
    [3, 7],       [4, 6, 8],    [5, 7]
]

def dls(curr, goal, limit, path, path_set):
    """
    Depth-Limited Search helper.
    Returns: (solution_path, cutoff_occurred)
    """
    if curr == goal:
        return path, False
    if len(path) - 1 == limit:
        return None, True  # Depth limit reached
    cutoff_occurred = False
    ind = curr.index(0)
    for target in MOVES[ind]:
        nxt = curr.copy()
        nxt[target], nxt[ind] = nxt[ind], nxt[target]
        nxt_tuple = tuple(nxt)
        if nxt_tuple not in path_set:
            path_set.add(nxt_tuple)
            result, cutoff = dls(nxt, goal, limit, path + [nxt], path_set)
            if result is not None:
                return result, False
            if cutoff:
                cutoff_occurred = True
            path_set.remove(nxt_tuple)  # Backtrack

    return None, cutoff_occurred


def ids(initial, goal, max_depth=35):
    """
    Iterative Deepening Search: repeatedly runs DLS with increasing limits.
    Returns: (solution_path, solved_depth)
    """
    for limit in range(max_depth):
        path_set = {tuple(initial)}
        result, cutoff = dls(initial, goal, limit, [initial], path_set)
        
        if result is not None:
            return result, limit  # limit is the depth where it was solved
        
        if not cutoff:
            # Entire reachable tree exhausted without hitting depth limit
            break

    return None, None

def print_pretty(state):
    for i in range(9):
        if i%3==2:  print(state[i])
        else:   print(state[i],end=' ')

# ==========================================
# Input and Execution
# ==========================================
initial = []
print("Enter initial state (9 numbers, 0 for blank):")
for i in range(9):
    initial.append(int(input(f"Tile {i + 1}: ")))
goal = []
print("Enter goal state (9 numbers, 0 for blank):")
for i in range(9):
    goal.append(int(input(f"Tile {i + 1}: ")))
print("\n--- Starting Iterative Deepening Search ---")
solution, solved_depth = ids(initial, goal)
if solution:
    print(f"\nSUCCESS: Puzzle solved at depth {solved_depth}!")
    print(f"Total moves: {len(solution) - 1}\n")
    for step_num, state in enumerate(solution):
        print(f"Step {step_num} (depth {step_num}):")
        print_pretty(state)
else:
    print("\nNo solution found (unsolvable configuration or exceeds max depth).")