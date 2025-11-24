# tic_tac_toe
Overview of the Project-
This is a classic implementation of the Tic-Tac-Toe (Noughts and Crosses) game, developed entirely in Python 3. It operates via the Command Line Interface (CLI) and serves as a robust example of procedural programming, state management using $2D$ lists, and basic AI implementation.
The project offers two modes of play:Player vs. Player or Player vs. Computer (Random AI)


Features-
Dual Game Modes: Supports both two-human-player competition and single-player games against a simple Random AI .
2D Board Representation: Uses a list of lists (board[r][c]) for intuitive mapping of the 3 cross 3.
Robust Input Validation: Utilizes try-except blocks to handle non-numeric input and ensures players only choose unoccupied spaces within the 1-9 range.
Clear Win/Draw Detection: Accurately checks all 8 winning combinations (rows, columns, diagonals) and handles draw conditions.
Modular Codebase: Game logic is encapsulated in separate functions (e.g., check_winner, get_player_move) for high maintainability.


Technologies/Tools used-
Python 3.x: The core programming language used for development.
Random Module: A standard Python library used specifically by the computer_move() function to select random, valid moves for the AI opponent.
Command Line Interface (CLI): The environment used for all user input and game output.


Steps to Install & Run the Project-
Prerequisites
You only need Python 3.x installed on your operating system.
Installation
Clone the Repository: Navigate to your desired directory and use Git to clone the project.
git clone https://github.com/YOUR_USERNAME/your-repo-name.git
cd your-repo-name
Run the Game: Execute the main script using the Python interpreter.
python tic_tac_toe.py


Gameplay Instructions-
When prompted, input a number from 1 to 9 corresponding to the position you want to mark on the board. The positions map as follows:
1 | 2 | 3
---+---+---
4 | 5 | 6
---+---+---
 7 | 8 | 9


Instructions for Testing-
You can verify the game's functionality by executing the following test scenarios:     
Core Game Flow Tests
Test Win Conditions: Play a game specifically targeting a vertical, horizontal, and diagonal win to confirm the check_winner function is flawless.
Test Draw Condition: Play a game where all nine squares are filled without creating a winning line, ensuring the board_full function correctly terminates the game as a draw.
Test AI Mode: Run the Player vs Computer mode several times to ensure the computer never attempts an illegal move (it only chooses from available empty spots).
 

Input Validation Tests-
Test the robustness of the get_player_move function:
Non-Numeric Input: Enter letters or symbols (e.g., A, !). The program should reject the input with an error message.
Out-of-Range Input: Enter numbers like 0 or 10. The program should reject the input, prompting for a number between 1 and 9.
Occupied Square: Try to mark a position that already has an 'X' or 'O'. The program should reject the move and ask for a new position


Screenshots-
<img width="504" height="995" alt="Screenshot 2025-11-24 200807" src="https://github.com/user-attachments/assets/5aef368b-5de1-49b2-968c-1317d31c1e2f" />



