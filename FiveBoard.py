# Author: Erika Tharp
# Date: 6/1/2020
# Description: This project includes a class called FiveBoard that represents .the board for a two-player game that is like tic-tac-toe, which is played on  a 15 x 15 board.
#              And each player is trying to get 5 in a row.
#              The class has two private data members: a list of lists that represents the board and the current state.
#              It also has a get method to obtain the current status and an init method to initialize the board to a list of 15 lists that each contain 15 empty strings (where each represents an empty square), and initializes the current_state to "UNFINISHED."
#              It also has  a method named make_move that takes three parameters, a row and a column where each is an integer in the range 0-14, and either 'x' or 'o' to indicate the player who is making the move.
#              If that square is already occupied, or if the game has already been won or drawn, make_move should return False.
#              Otherwise, it records the move, update the current_state, and return True.
#              It's possible for multiple moves to be made in a row for the same player.
#              A game is drawn when all of the squares are filled, but neither player has won.


class FiveBoard:
    """
    Represents the board for a two-player game that is like tic-tac-toe, which is played on  a 15 x 15 board with two private data members and two functions called get_current_state and make_move.
    """

    def __init__(self):
        """Creates an object with a list of lists that represents the board, and the current state."""
        self._board_list = [["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
                            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
                            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
                            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
                            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
                            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
                            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
                            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
                            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
                            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
                            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
                            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
                            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
                            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ],
                            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ]
                            ]
        self._current_state = "UNFINISHED"

    def get_current_state(self):
        """
        Returns the current state. "X_WON", "O_WON", "DRAW", or 'UNFINISHED'
        """
        return self._current_state

    def make_move(self, row, col, player):
        """
        Takes three parameters, a row and a column where each is an integer in the range 0-14, and either 'x' or 'o' to indicate the player who is making the move.
        If that square is already occupied, or if the game has already been won or drawn, make_move should return False.
        Otherwise, it records the move, update the current_state, and return True.
        A game is drawn when all of the squares are filled, but neither player has won.
        """

        # Check whether the square is occupied.
        if self._board_list[row][col] == "" and self._current_state == "UNFINISHED":
            # Occupy that square.
            self._board_list[row][col] = player
            # Check if there are any 5 consecutive xs and os.
            empty_square_counter = 0
            for row in range(0, 14):
                for col in range(0, 14):
                    # Check for x horizontally
                    if self._board_list[row][col] == "x" and self._board_list[row][col + 1] == self._board_list[row][
                        col] and self._board_list[row][col + 2] == self._board_list[row][col] and self._board_list[row][
                        col + 3] == self._board_list[row][col] and self._board_list[row][col] == self._board_list[row][col + 4]:
                        self._current_state = "X_WON"
                        return False
                    # Check for x vertically
                    elif self._board_list[row][col] == "x" and self._board_list[row + 1][col] == self._board_list[row][
                        col] and self._board_list[row + 2][col] == self._board_list[row][col] and \
                            self._board_list[row + 3][
                                col] == self._board_list[row][col] and self._board_list[row][col] == \
                            self._board_list[row + 4][
                                col]:
                        self._current_state = "X_WON"
                        return False
                    # Check for x diagonally
                    elif self._board_list[row][col] == "x" and self._board_list[row + 1][col + 1] == \
                            self._board_list[row][
                                col] and self._board_list[row + 2][col + 2] == self._board_list[row][col] and \
                            self._board_list[row + 3][
                                col + 3] == self._board_list[row][col] and self._board_list[row][col] == \
                            self._board_list[row + 4][
                                col + 4]:
                        self._current_state = "X_WON"
                        return False
                    # Check for o horizontally
                    elif self._board_list[row][col] == "o" and self._board_list[row][col + 1] == self._board_list[row][
                        col] and self._board_list[row][col + 2] == self._board_list[row][col] and self._board_list[row][
                        col + 3] == self._board_list[row][col] and self._board_list[row][col] == self._board_list[row][
                        col + 4]:
                        self._current_state = "O_WON"
                        return False
                    # Check for o vertically.
                    elif self._board_list[row][col] == "o" and self._board_list[row + 1][col] == self._board_list[row][
                        col] and self._board_list[row + 2][col] == self._board_list[row][col] and \
                            self._board_list[row + 3][
                                col] == self._board_list[row][col] and self._board_list[row][col] == \
                            self._board_list[row + 4][
                                col]:
                        self._current_state = "O_WON"
                        return False
                    # Check for o diagonally
                    elif self._board_list[row][col] == "o" and self._board_list[row + 1][col + 1] == \
                            self._board_list[row][
                                col] and self._board_list[row + 2][col + 2] == self._board_list[row][col] and \
                            self._board_list[row + 3][
                                col + 3] == self._board_list[row][col] and self._board_list[row][col] == \
                            self._board_list[row + 4][
                                col + 4]:
                        self._current_state = "O_WON"
                        return False
                    elif self._board_list[row][col] == "":
                        empty_square_counter += 1
            if empty_square_counter == 0 and self._current_state == "X_WON" and self._current_state == "O_WON":
                self._current_state = "DRAW"
                return False
        return True
