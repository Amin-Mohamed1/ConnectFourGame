# **ConnectFourGame**

This repository contains **ConnectFourGame**, a web-based project developed using **Flask** for the **CSE351: Introduction to Artificial Intelligence** course. The project aims to implement a dynamic and interactive **Connect Four** game with two modes of play: **Human vs. Human** and **Human vs. AI**. The AI is powered by the **Minimax algorithm** and its variations, including **Alpha-Beta Pruning** and **ExpectiMinimax**, to provide a challenging and engaging experience.

---

## **Features**

### 🎮 **Game Modes**
1. **Human vs. Human**  
   Two players can compete locally, taking turns to drop discs into the Connect Four grid.

2. **Human vs. AI**  
   Challenge the AI agent, which uses advanced algorithms to make strategic moves:
   - **Minimax**: Explores all possible moves to select the optimal one.
   - **Alpha-Beta Pruning**: Optimizes Minimax by pruning unnecessary branches, reducing computation time.
   - **ExpectiMinimax**: Considers probabilistic outcomes, making it suitable for scenarios with uncertainty or randomness.

---

### 🧠 **AI Capabilities**
- **Minimax Algorithm**: Evaluates all possible moves to determine the best one.
- **Alpha-Beta Pruning**: Enhances Minimax by pruning branches that don't need to be explored, improving efficiency.
- **ExpectiMinimax**: Extends Minimax to handle stochastic elements by considering probabilistic outcomes.
- **Depth-limited Search**: Limits the depth of the search tree to balance between computation time and decision accuracy.
- **Heuristic Evaluation**: Custom heuristics to evaluate non-terminal game states, enhancing the AI's decision-making.
- **Adaptive Difficulty**: Adjust AI difficulty by modifying the search depth and heuristic evaluation.

---

## **Technologies Used**
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **AI Algorithms**: Minimax, Alpha-Beta Pruning, ExpectiMinimax
---
