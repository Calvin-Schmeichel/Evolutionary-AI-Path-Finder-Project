# Import random for generating random choices
import random
# Import time for adding delays (animations)
import time


# Define the Board class to encapsulate the game environment
class Board:
    # Initialize the game board with size, player, target, and walls
    def __init__(self, size=10):
        self.size = size
        # Create a square grid for the board initialized with '.'
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        # Set player's starting position
        self.player_pos = [size-1, 0]
        # Set target's position
        self.target_pos = [0, size-1]
        # Define positions for walls on the board
        self.wall_pos = [(size//2 - 1, size//2 - 1), (size//2, size//2 - 1), 
                         (size//2 - 1, size//2), (size//2, size//2)]
    # Setup the board with walls, player, and target positions
        self.setup_board()

    # Setup the board with walls, player, and target positions
    def setup_board(self):
        # Define positions for walls on the board
        for row, col in self.wall_pos:
            # Marking wall positions with 'W'
            self.board[row][col] = 'W'
        # Set player's starting position
        self.board[self.player_pos[0]][self.player_pos[1]] = 'P'
        # Set target's position
        self.board[self.target_pos[0]][self.target_pos[1]] = 'T'

    def move_player_random(self):
        directions = ['up', 'down', 'left', 'right']
        return self.move_player(random.choice(directions))

    def move_player(self, direction):
        # Set player's starting position
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
        # Define positions for walls on the board
            (new_pos[0], new_pos[1]) not in self.wall_pos):
        # Set player's starting position
            self.board[self.player_pos[0]][self.player_pos[1]] = '.'
        # Set player's starting position
            self.player_pos = new_pos
        # Set player's starting position
            self.board[self.player_pos[0]][self.player_pos[1]] = 'P'
        # Marking the target's position with 'T'
            return True
        return False

    def is_at_target(self):
        # Set player's starting position
        return self.player_pos == self.target_pos

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

def run_simulation(iterations=100000):
    best_steps = float('inf')
    best_path = []
    for _ in range(iterations):
        board = Board()
        steps = 0
        path = []
        while not board.is_at_target():
            if board.move_player_random():
                path.append(board.player_pos.copy())
            steps += 1
            if steps >= best_steps:
                break
        if board.is_at_target() and steps < best_steps:
            best_steps = steps
            best_path = path.copy()

    return best_steps, best_path

def animate_path(board, path):
    print("Animating the best path taken:")
    time.sleep(1)
    for pos in path:
        board.board = [['.' for _ in range(board.size)] for _ in range(board.size)]
        for row, col in board.wall_pos:
            board.board[row][col] = 'W'
        # Marking the player's position with 'P'
        board.board[pos[0]][pos[1]] = 'P'
        # Marking the target's position with 'T'
        board.board[board.target_pos[0]][board.target_pos[1]] = 'T'
        board.print_board()
        time.sleep(0.1)

    # After animation, print the final path with ASCII arrows
    print_final_path(board, path)

def print_final_path(board, path):
    # Setup the board with walls, player, and target positions
    board.setup_board()  # Reset board
    arrows = {'up': '↑', 'down': '↓', 'left': '←', 'right': '→'}
    
    # Determine direction for each move and place arrows
    for i in range(len(path) - 1):
        curr_pos, next_pos = path[i], path[i + 1]
        if next_pos[0] < curr_pos[0]: direction = 'up'
        elif next_pos[0] > curr_pos[0]: direction = 'down'
        elif next_pos[1] < curr_pos[1]: direction = 'left'
        elif next_pos[1] > curr_pos[1]: direction = 'right'
        board.board[curr_pos[0]][curr_pos[1]] = arrows[direction]
    # Ensure the target is correctly marked after placing arrows
        # Marking the target's position with 'T'
    board.board[board.target_pos[0]][board.target_pos[1]] = 'T'

        # Marking the player's position with 'P'
    # Print the number of steps and the final board with ASCII arrows
    print(f"Final best path took {len(path)} steps.")
    board.print_board()

# After running the simulation and get the best result and path
best_result, best_path = run_simulation()
        # Marking the target's position with 'T'
print(f"The fewest steps taken to reach the target in 100 simulations was: {best_result}")

# Initialize a new board and animate the best path
board = Board()
animate_path(board, best_path)