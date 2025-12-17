# 🧩 8-Puzzle Game with AI Solver

This project is an implementation of the classic **8-Puzzle problem**.
It allows the user to play the puzzle manually or solve it automatically
using an Artificial Intelligence search algorithm.

The application is built using **Python** and **Streamlit**, providing a
simple web-based interface that is easy to use and interactive.

---

## 📌 Features

- Interactive 3×3 puzzle board
- Manual tile movement by clicking tiles
- Automatic puzzle solving using **A\*** search
- Optimal solution using a heuristic-based approach
- Clean and minimal graphical user interface (GUI)

---

## 🧠 Algorithm Used

### A* Search Algorithm
A* is an informed search algorithm that finds the optimal solution by
combining:
- **g(n):** the cost to reach the current state
- **h(n):** a heuristic estimate of the remaining cost

The heuristic used in this project is **Manhattan Distance**, which
calculates how far each tile is from its goal position.
This significantly reduces the number of explored states compared to
uninformed search algorithms.

---

## 🛠️ Technologies Used

- Python
- Streamlit

---

## 🌐 Live Demo

The project is deployed using **Streamlit Community Cloud**  
and can be accessed here:

🔗 https://ai-puzzle-mgnntvsubsmf7h2sec84gb.streamlit.app/

---

## ▶️ How to Run the Project Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/USERNAME/REPOSITORY_NAME.git
