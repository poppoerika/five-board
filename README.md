# Five Board


FiveBoard that represents the board for a two-player game that is like [tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe), but on a larger scale.  Instead of a 3x3 board, it is played on a 15x15 board, and instead of 3 in a row, each player is trying to get 5 in row.

The class has two **private** data members - a list of lists that represents the board, and the current state, which holds one of the four following values: "X_WON", "O_WON", "DRAW", or "UNFINISHED".  It should have a get method named get_current_state, which returns the current state.

The class has an init method that initializes the board to a list of 15 lists that each contain 15 empty strings (where each represents an empty square), and initializes the current_state to "UNFINISHED".

It has a method named make_move that takes three parameters, a row and a column (in that order) where each is an integer in the range 0-14, and either 'x' or 'o' to indicate the player who is making the move. If that square is already occupied, or if the game has already been won or drawn, make_move should return False. Otherwise, it should record the move, update the current_state, and return True. **It's possible for multiple moves to be made in a row for the same player (so you don't need to enforce alternating turns).** A game is drawn when all of the squares are filled, but neither player has won.


Example
```
board = FiveBoard()
board.make_move(0, 0, 'o')
board.make_move(6, 5, 'x')
board.make_move(2, 1, 'x')
board.make_move(3, 2, 'x')
board.get_current_state()
```
