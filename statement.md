Problem Statement-
The objective of this project is to successfully implement the classic game of Tic-Tac-Toe (Noughts and Crosses) as a functional, console-based application utilizing the Python programming language. The primary technical challenge lies in developing robust game logic that can accurately manage the 3 cross 3 game board state, handle player turns, ensure proper input validation, and definitively check for all nine possible win conditions (three horizontal, three vertical, and two diagonal lines) or a draw state. This project serves as a practical demonstration of foundational Python programming skills and logical state management.
Scope of the Project-
The project is defined as a Minimum Viable Product (MVP) focusing strictly on core gameplay functionality:
Platform: Console/Terminal-based application. A Graphical User Interface (GUI) is out of scope.
Game Mode: Player vs. Player (PvP) only. Implementation of an Artificial Intelligence (AI) opponent is out of scope.
Technology: Pure Python using standard library features. The project aims to have zero external dependencies.
Output: The application must successfully run from a terminal prompt and provide clear, text-based feedback to the users regarding the board state and game outcomes.
Target Users-
Beginner Python Developers: Individuals seeking a clear, self-contained, and manageable project to study and practice fundamental Python concepts such as functions, lists (for board representation), loops, and conditional statements.
Casual Users: Anyone looking for a quick and simple game of Tic-Tac-Toe that can be played immediately on the command line without complex setup or dependencies.
High-Level Features-
The application will include the following high-level capabilities:
Game Board Representation: A clear, text-based 3 cross 3 grid displayed in the console, providing a visual representation of the game's current state.
Two-Player Mode: Supports two human players (designated as 'X' and 'O') with automated, alternating turns.
Turn Management and Input:Prompts the current player to input their move, typically using a coordinate system or square number.Automatically switches the turn after a valid move is made.
Input Validation System: Guards against invalid moves by rejecting attempts to:Place a marker outside the 3 cross 3 board boundaries.Overwrite a square that has already been marked.
Game Termination Logic:
Win Detection: Implements comprehensive logic to detect and immediately announce the winning player when a 3-in-a-row is achieved (horizontally, vertically, or diagonally).
Draw Detection: Recognizes and announces a Draw if the board is completely full and no player has secured a winning alignment.
Game Restart Option: Provides the user with an option to easily initiate a new game after the current one concludes.
