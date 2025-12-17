import random
from heapq import heappush, heappop

#! GOAL 
GOAL = (1,2,3,
        4,5,6,
        7,8,0)

#! Heuristic 
def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i]==0:
            continue
        goal_index = GOAL.index(state[i])
        distance += abs(i//3 - goal_index//3) + abs(i%3 - goal_index%3)
    return distance

#!  Moves
def get_neighbors(state):
    neighbors = []
    index = state.index(0)
    row, col = index//3, index%3
    moves = [(1,0),(-1,0),(0,1),(0,-1)]
    for dx, dy in moves:
        nx, ny = row+dx, col+dy
        if 0<=nx<3 and 0<=ny<3:
            new_index = nx*3 + ny
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(tuple(new_state))
    return neighbors

#! A* Algorithm 
def astar(start):
    open_list = []
    heappush(open_list, (0, start))
    came_from = {}
    g = {start:0}

    while open_list:
        _, current = heappop(open_list)
        if current == GOAL:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in get_neighbors(current):
            new_cost = g[current]+1
            if neighbor not in g or new_cost < g[neighbor]:
                g[neighbor] = new_cost
                f = new_cost + heuristic(neighbor)
                heappush(open_list, (f, neighbor))
                came_from[neighbor] = current
    return None

#! Grid Printing 
def print_grid(state):
    for i in range(3):
        row = ""
        for j in range(3):
            val = state[i*3 + j]
            row += " " if val==0 else str(val)
            row += " "
        print(row)
    print()

#! Shuffle 
def shuffle(state):
    state = list(GOAL)
    for _ in range(30):
        neighbors = get_neighbors(tuple(state))
        state = list(random.choice(neighbors))
    return tuple(state)

#!Main Game
state = shuffle(GOAL)

while True:
    print_grid(state)
    move = input("Move (w/a/s/d) or solve (enter 'solve'): ").strip().lower()
    
    if move == "solve":
        path = astar(state)
        if path:
            print("Solving...")
            for step in path[1:]:
                state = step
                print_grid(state)
        else:
            print("No solution found!")
        break

    zero_idx = state.index(0)
    row, col = zero_idx//3, zero_idx%3
    new_row, new_col = row, col

    if move == "w":
        new_row -= 1
    elif move == "s":
        new_row += 1
    elif move == "a":
        new_col -= 1
    elif move == "d":
        new_col += 1
    else:
        print("Invalid move!")
        continue

    if 0 <= new_row < 3 and 0 <= new_col < 3:
        new_idx = new_row*3 + new_col
        new_state = list(state)
        new_state[zero_idx], new_state[new_idx] = new_state[new_idx], new_state[zero_idx]
        state = tuple(new_state)
    else:
        print("Move out of bounds!")
