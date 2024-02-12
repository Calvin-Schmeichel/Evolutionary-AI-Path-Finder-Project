import random

class Board:
    def __init__(self, size=10):  # Adjusted board size to 10x10
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.player_pos = [size-1, 0]  # Player starts at bottom left
        self.target_pos = [0, size-1]  # Target is at top right
        # Adjusting wall position for a smaller board
        self.wall_pos = [(size//2 - 1, size//2 - 1), (size//2, size//2 - 1), 
                         (size//2 - 1, size//2), (size//2, size//2)]
        self.setup_board()

    def setup_board(self):
        for row, col in self.wall_pos:
            self.board[row][col] = 'W'
        self.board[self.player_pos[0]][self.player_pos[1]] = 'P'
        self.board[self.target_pos[0]][self.target_pos[1]] = 'T'

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def move_player_random(self):
        directions = ['up', 'down', 'left', 'right']
        return self.move_player(random.choice(directions))

    def move_player(self, direction):
        new_pos = self.player_pos.copy()
        if direction == 'up':
            new_pos[0] -= 1
        elif direction == 'down':
            new_pos[0] += 1
        elif direction == 'left':
            new_pos[1] -= 1
        elif direction == 'right':
            new_pos[1] += 1

        if (0 <= new_pos[0] < self.size and 0 <= new_pos[1] < self.size and 
            (new_pos[0], new_pos[1]) not in self.wall_pos):
            self.board[self.player_pos[0]][self.player_pos[1]] = '.'
            self.player_pos = new_pos
            self.board[self.player_pos[0]][self.player_pos[1]] = 'P'
            return True
        return False

    def is_at_target(self):
        return self.player_pos == self.target_pos

    def calculate_score(self):
        distance = abs(self.player_pos[0] - self.target_pos[0]) + abs(self.player_pos[1] - self.target_pos[1])
        return max(0, self.size - distance)  # Score based on closeness to target

def explore_without_knowledge(board, move_limit=9999):
    steps = 0
    while steps < move_limit and not board.is_at_target():
        board.move_player_random()
        steps += 1
    board.print_board()
    if board.is_at_target():
        print(f"Target reached in {steps} steps.")
    else:
        print(f"Player died after {steps} moves.")
    score = board.calculate_score()
    print(f"Final score (based on closeness to target): {score}")

# Initialize and run the simulation
board = Board()
board.print_board()
explore_without_knowledge(board)
