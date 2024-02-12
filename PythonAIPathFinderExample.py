class Board:
    def __init__(self, size=20):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.player_pos = [size-1, 0]  # Player starts at bottom left
        self.target_pos = [0, size-1]  # Target is at top right
        self.wall_pos = [(size//2 - 1, size//2 - 1), (size//2, size//2 - 1), 
                         (size//2 - 1, size//2), (size//2, size//2)]  # 2x2 wall in the middle
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

    def move_player(self, direction):
        # Calculate new position based on direction
        new_pos = self.player_pos.copy()
        if direction == 'up':
            new_pos[0] -= 1
        elif direction == 'down':
            new_pos[0] += 1
        elif direction == 'left':
            new_pos[1] -= 1
        elif direction == 'right':
            new_pos[1] += 1

        # Check for wall collision or out of bounds
        if (0 <= new_pos[0] < self.size and 0 <= new_pos[1] < self.size and 
            (new_pos[0], new_pos[1]) not in self.wall_pos):
            # Move is valid, update player's position
            self.board[self.player_pos[0]][self.player_pos[1]] = '.'
            self.player_pos = new_pos
            self.board[self.player_pos[0]][self.player_pos[1]] = 'P'
            return True
        return False

    def is_at_target(self):
        return self.player_pos == self.target_pos

def simple_ai_pathfinder(board):
    steps = 0
    while not board.is_at_target():
        if board.player_pos[0] > board.target_pos[0]:
            board.move_player('up')
        elif board.player_pos[1] < board.target_pos[1]:
            board.move_player('right')
        board.print_board()
        steps += 1
        if steps > 100:  # Prevent infinite loops
            print("Failed to reach target within step limit.")
            break
    if board.is_at_target():
        print(f"Target reached in {steps} steps.")

# Initialize and run the simulation
board = Board()
board.print_board()
simple_ai_pathfinder(board)
