import random

class Board:
    def __init__(self, size=10):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.player_pos = [size-1, 0]  # Player starts at bottom left
        self.target_pos = [0, size-1]  # Target is at top right
        self.wall_pos = [(size//2 - 1, size//2 - 1), (size//2, size//2 - 1), 
                         (size//2 - 1, size//2), (size//2, size//2)]  # Walls in the center
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

def run_simulation(iterations=100):
    best_steps = float('inf')
    for _ in range(iterations):
        board = Board()
        steps = 0
        while not board.is_at_target():
            board.move_player_random()
            steps += 1
            if steps >= best_steps:
                break  # Stop current game if it exceeds the best step count
        if board.is_at_target():
            best_steps = min(best_steps, steps)

    return best_steps

# Run the simulation 100 times and get the best result
best_result = run_simulation()
print(f"The fewest steps taken to reach the target in 100 simulations was: {best_result}")
