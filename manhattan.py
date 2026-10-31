import heapq

# Target goal state
GOAL_STATE = (1, 2, 3, 
              4, 5, 6, 
              7, 8, 0)

def manhattan_distance(state):
    """Calculate total Manhattan distance for non-zero tiles."""
    distance = 0
    for idx, tile in enumerate(state):
        if tile != 0:
            # Current row and column
            r1, c1 = idx // 3, idx % 3
            
            # Target row and column (1-based index mapped to 0-based)
            target_idx = tile - 1
            r2, c2 = target_idx // 3, target_idx % 3
            
            distance += abs(r1 - r2) + abs(c1 - c2)
    return distance

def get_neighbors(state):
    """Generate all valid next states by moving the blank tile (0)."""
    neighbors = []
    zero_idx = state.index(0)
    row, col = zero_idx // 3, zero_idx % 3

    # Moves: Up, Down, Left, Right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        nr, nc = row + dr, col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_zero_idx = nr * 3 + nc
            state_list = list(state)
            
            # Swap blank space with adjacent tile
            state_list[zero_idx], state_list[new_zero_idx] = (
                state_list[new_zero_idx],
                state_list[zero_idx],
            )
            neighbors.append(tuple(state_list))

    return neighbors

def solve_8_puzzle(initial_state):
    """Solve 8-puzzle using A* Search with Manhattan Distance."""
    # Priority Queue stores tuples of: (f_score, g_score, current_state, path)
    initial_h = manhattan_distance(initial_state)
    open_set = [(initial_h, 0, initial_state, [initial_state])]
    
    # Track lowest g_score visited for each state
    visited = {initial_state: 0}

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == GOAL_STATE:
            return path

        # Skip if we already found a shorter path to this state
        if g > visited[current]:
            continue

        for neighbor in get_neighbors(current):
            new_g = g + 1
            if neighbor not in visited or new_g < visited[neighbor]:
                visited[neighbor] = new_g
                h = manhattan_distance(neighbor)
                heapq.heappush(open_set, (new_g + h, new_g, neighbor, path + [neighbor]))

    return None

def print_board(state):
    """Format and print a 3x3 board."""
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Example Usage
if __name__ == "__main__":
    # 0 represents the empty space
    initial_board = (1, 2, 3, 
                     4, 0, 5, 
                     7, 8, 6)

    solution_path = solve_8_puzzle(initial_board)

    if solution_path:
        print(f"Solvable in {len(solution_path) - 1} moves:\n")
        for step, state in enumerate(solution_path):
            print(f"Step {step}:")
            print_board(state)
    else:
        print("No solution found.")