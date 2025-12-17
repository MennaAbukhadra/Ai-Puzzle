import streamlit as st
import random
import time
from heapq import heappush, heappop

#! Page setup
st.set_page_config(page_title="8-Puzzle Game", layout="centered")

st.title("🧩 8-Puzzle Game")
st.caption("Play manually or solve using A* Search Algorithm")

st.divider()

#! Goal state
GOAL = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

#! Manhattan Distance heuristic
def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            gi = GOAL.index(state[i])
            distance += abs(i//3 - gi//3) + abs(i%3 - gi%3)
    return distance

#! Generate neighbors
def get_neighbors(state):
    neighbors = []
    index = state.index(0)
    row, col = index//3, index%3
    moves = [(1,0), (-1,0), (0,1), (0,-1)]

    for dx, dy in moves:
        nx, ny = row + dx, col + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_index = nx*3 + ny
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(tuple(new_state))
    return neighbors

#! A* search algorithm
def astar(start):
    open_list = []
    heappush(open_list, (0, start))
    came_from = {}
    g = {start: 0}

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
            new_cost = g[current] + 1
            if neighbor not in g or new_cost < g[neighbor]:
                g[neighbor] = new_cost
                f = new_cost + heuristic(neighbor)
                heappush(open_list, (f, neighbor))
                came_from[neighbor] = current
    return None

#! Shuffle puzzle (always solvable)
def shuffle():
    state = list(GOAL)
    for _ in range(30):
        state = list(random.choice(get_neighbors(tuple(state))))
    return tuple(state)

#! Session state
if "state" not in st.session_state:
    st.session_state.state = shuffle()

#! Placeholder for animation
board_placeholder = st.empty()

#! Draw puzzle function
def draw_board(state):
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            val = state[i*3 + j]
            if val == 0:
                cols[j].button(
                    "",
                    disabled=True,
                    use_container_width=True,
                    key=f"e-{i}-{j}-{time.time()}"
                )
            else:
                cols[j].button(
                    str(val),
                    disabled=True,
                    use_container_width=True,
                    key=f"t-{i}-{j}-{time.time()}"
                )

#! Manual play (normal buttons)
st.subheader("🎮 Play")

for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        val = st.session_state.state[i*3 + j]

        if val == 0:
            cols[j].button("", disabled=True, use_container_width=True)
        else:
            if cols[j].button(str(val), key=f"{i}-{j}", use_container_width=True):
                zero = st.session_state.state.index(0)
                zi, zj = zero//3, zero%3
                if abs(zi - i) + abs(zj - j) == 1:
                    new_state = list(st.session_state.state)
                    new_state[zero], new_state[i*3 + j] = new_state[i*3 + j], new_state[zero]
                    st.session_state.state = tuple(new_state)
                    st.rerun()

#! Solved message
if st.session_state.state == GOAL:
    st.success("🎉 Puzzle Solved!")

st.divider()

#! Controls
c1, c2 = st.columns(2)

with c1:
    if st.button("🤖 Solve using A*"):
        path = astar(st.session_state.state)
        if path:
            for step in path:
                board_placeholder.container()
                with board_placeholder:
                    draw_board(step)
                time.sleep(0.25)  # smooth continuous animation
            st.session_state.state = path[-1]
            st.rerun()

with c2:
    if st.button("🔄 Shuffle"):
        st.session_state.state = shuffle()
        st.rerun()
