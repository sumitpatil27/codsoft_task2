# codsoft_task2

# 🎮 Tic-Tac-Toe AI Game (CODSOFT Task)

## 📌 Project Description

This project is a console-based Tic-Tac-Toe game developed using Python.  
The game allows a human player (X) to play against an AI opponent (O).

The AI uses the Minimax Algorithm to make optimal moves, ensuring it never loses.

---

## 🚀 Features

- Human vs AI gameplay
- AI powered by Minimax Algorithm
- Detects win conditions
- Detects draw condition
- Prevents invalid moves
- Simple console interface

---

## 🛠️ Technologies Used

- Python 3
- math module

---

## 🧠 Algorithm Used

### Minimax Algorithm

The Minimax algorithm is used to determine the best possible move for the AI.  

- If AI wins → score = +1  
- If Player wins → score = -1  
- If Draw → score = 0  

The AI evaluates all possible future moves and chooses the optimal one.

This ensures:
- AI never loses
- AI always plays optimally

---

## 📂 Project Structure

codsoft_task2/
│
├── tictactoe.py
└── README.md


---

## ▶️ How to Run the Project

1. Make sure Python is installed.
2. Save the file as `tictactoe.py`
3. Open terminal or command prompt.
4. Navigate to the project folder.
5. Run:

python tictactoe.py


---

## 🎯 How to Play

- You are **X**
- AI is **O**
- Enter position number between **0 and 8**

Board positions:

0 | 1 | 2
3 | 4 | 5
6 | 7 | 8


Choose the number corresponding to the position where you want to place X.

---

## 💬 Example Gameplay

Tic-Tac-Toe (You = X, AI = O)

| |
| |
| |

Enter position (0-8): 0


Game continues until:
- You win
- AI wins
- Or it's a draw

---

## 📌 Internship Task

This project is developed as part of the CODSOFT Internship Program.
