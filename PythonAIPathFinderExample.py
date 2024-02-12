import random
import time

class Board:
    def __init__(self, size=10):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.player_pos = [size-1, 0]
        self.target_pos = [0, size-1]
        self.wall_pos = [(size//2 - 1, size//2 - 1), (size//2, size//2 - 1), 
                         (size//2 - 1, size//2), (size//2, size//2)]
        self.setup_board()

    def setup_board(self):
        for row, col in self.wall_pos:
            self.board[row][col] = 'W'
        self.board[self.player_pos[0]][self.player_pos[1]] = 'P'
        self.board[self.target_pos[0]][self.target_pos[1]] = 'T'

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

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

def run_simulation(iterations=100):
    best_steps = float('inf')
    best_path = []
    for _ in range(iterations):
        board = Board()
        steps = 0
        path = []
        while not board.is_at_target():
            if board.move_player_random():
                path.append(board.player_pos.copy())  # Store each successful move
            steps += 1
            if steps >= best_steps:
                break
        if board.is_at_target() and steps < best_steps:
            best_steps = steps
            best_path = path.copy()

    return best_steps, best_path

def animate_path(board, path):
    print("Animating the best path taken:")
    time.sleep(1)  # Wait a second before starting the animation
    for pos in path:
        board.board = [['.' for _ in range(board.size)] for _ in range(board.size)]
        for row, col in board.wall_pos:
            board.board[row][col] = 'W'
        board.board[pos[0]][pos[1]] = 'P'
        board.board[board.target_pos[0]][board.target_pos[1]] = 'T'
        board.print_board()
        time.sleep(0.1)  # Delay between steps for animation

# Run the simulation 100 times and get the best result and path
best_result, best_path = run_simulation()
print(f"The fewest steps taken to reach the target in 100 simulations was: {best_result}")

# Initialize a new board and animate the best path
board = Board()
animate_path(board, best_path)
