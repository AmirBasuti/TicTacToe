import os


class TicTacToe:
    def __init__(self):
        self.message = None
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turn_symbol = 1
        self.move = []
        self.source_symbol_iso = {
            0: ' ',
            1: 'X',
            2: 'O'
        }

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        if self.message:
            print(self.message)
            self.message = None

        for row in self.board:
            print(' | '.join([self.source_symbol_iso[i] for i in row]))

    def is_valid_move(self, row, col):
        if self.board[row][col] != 0:
            self.message = 'Invalid move, please try another row or column'
            return False
        return True

    def update_board(self, row, col):
        self.board[row][col] = self.turn_symbol
        self.move.append((row, col))

    def check_winner(self, row, col):
        diag_win = rev_diag_win = False
        row_win = all(self.board[row][i] == self.turn_symbol for i in range(3))
        col_win = all(self.board[i][col] == self.turn_symbol for i in range(3))
        if row == col or row + col == 2:
            diag_win = all(self.board[i][i] == self.turn_symbol for i in range(3))
            rev_diag_win = all(self.board[i][2 - i] == self.turn_symbol for i in range(3))
        return row_win or col_win or diag_win or rev_diag_win

    def switch_turn(self):
        self.turn_symbol = 1 if self.turn_symbol == 2 else 2

    def make_move(self, row, col):
        if not self.is_valid_move(row, col):
            return

        self.update_board(row, col)

        if self.check_winner(row, col):
            return self.turn_symbol

        self.switch_turn()


class Player:
    def __init__(self, name, symbol):
        self._name = name
        self._symbol = symbol
        self._win = 0

    def __str__(self):
        return self._name

    @property
    def win(self):
        return self._win

    @win.setter
    def win(self, value):
        self._win = value


class Game:
    def __init__(self):
        self.player1 = Player('Player1', 1)
        self.player2 = Player('Player2', 2)
        self.list_players = {1: self.player1, 2: self.player2}
        self.tic_tac_toe = TicTacToe()

    def start_game(self):
        while True:
            self.tic_tac_toe.print_board()
            row = int(input('Enter row: '))
            col = int(input('Enter col: '))
            winner = self.tic_tac_toe.make_move(row, col)

            if winner:
                winer_player = self.list_players.get(winner)
                self.tic_tac_toe.print_board()
                winer_player.win += 1
                print(f'player {winer_player} wins {winer_player.win}!')
                break


if __name__ == '__main__':
    game = Game()
    game.start_game()
