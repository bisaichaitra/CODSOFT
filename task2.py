import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initialize empty board

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, move, player):
        self.board[move] = player

    def is_winner(self, player):
        # Check rows
        for i in range(0, 9, 3):
            if all(self.board[i+j] == player for j in range(3)):
                return True
        # Check columns
        for i in range(3):
            if all(self.board[i+j] == player for j in range(0, 9, 3)):
                return True
        # Check diagonals
        if all(self.board[i] == player for i in range(0, 9, 4)) or \
           all(self.board[i] == player for i in range(2, 7, 2)):
            return True
        return False

    def is_board_full(self):
        return ' ' not in self.board

    def game_over(self):
        return self.is_winner('X') or self.is_winner('O') or self.is_board_full()

    def minimax(self, board, depth, maximizing_player):
        if self.is_winner('X'):
            return -10 + depth
        elif self.is_winner('O'):
            return 10 - depth
        elif self.is_board_full():
            return 0

        if maximizing_player:
            best_score = float('-inf')
            for move in self.available_moves():
                board[move] = 'O'
                score = self.minimax(board, depth + 1, False)
                board[move] = ' '
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.available_moves():
                board[move] = 'X'
                score = self.minimax(board, depth + 1, True)
                board[move] = ' '
                best_score = min(score, best_score)
            return best_score

    def find_best_move(self):
        best_score = float('-inf')
        best_move = None
        for move in self.available_moves():
            self.board[move] = 'O'
            score = self.minimax(self.board, 0, False)
            self.board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move
        return best_move


def play_game():
    game = TicTacToe()
    human_player = 'X'
    ai_player = 'O'

    current_player = human_player if random.choice([True, False]) else ai_player

    while not game.game_over():
        if current_player == human_player:
            game.print_board()
            move = int(input("Enter your move (0-8): "))
            if move not in game.available_moves():
                print("Invalid move, try again.")
                continue
            game.make_move(move, human_player)
            current_player = ai_player
        else:
            print("AI is making a move...")
            ai_move = game.find_best_move()
            game.make_move(ai_move, ai_player)
            current_player = human_player

    game.print_board()
    if game.is_winner(human_player):
        print("Congratulations! You win!")
    elif game.is_winner(ai_player):
        print("AI wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    play_game()

