import random
from player import Player

class Board:
    def __init__(self, rows, columns):
        self.columns = columns
        self.rows = rows
        self.players = []
        self.grid = None
        self.reset_grid()

    def reset_grid(self):
        self.grid = [['.' for _ in range(self.columns)] for _ in range(self.rows)]

    def render_board(self):
        print('\n' * 50)
        for row in self.grid:
            for cell in row:
                print(cell, end=' ')
            print()

    def is_cell_free(self, row, col):
        return self.grid[row][col] == '.'

    def create_player(self):
        t_player_name = input('Player name: ')
        t_player_symbol = input('Player symbol: ')

        while True:
            t_player_pos_r = random.randint(0, self.rows - 1)
            t_player_pos_c = random.randint(0, self.columns - 1)
            if self.is_cell_free(t_player_pos_r, t_player_pos_c):
                break

        self.players.append(Player(t_player_name, t_player_symbol, t_player_pos_c, t_player_pos_r))
        self.update_grid()
        self.render_board()

    def update_grid(self):
        self.reset_grid()
        for player in self.players:
            self.grid[player.pos_r][player.pos_c] = player.symbol

    def move_player(self, player_name):
        player = next((p for p in self.players if p.name == player_name), None)

        if player is None:
            print(f"Player '{player_name}' not found.")
            return

        while True:
            self.render_board()
            move = input(f'{player.name}, move your player (W,A,S,D) or quit (Q): ').strip().lower()

            # Direções mapeadas para (delta_row, delta_col)
            direction_map = {
                'w': (-1, 0),  # cima
                's': (1, 0),  # baixo
                'a': (0, -1),  # esquerda
                'd': (0, 1)  # direita
            }

            if move == 'q':
                break

            if move not in direction_map:
                print("Invalid move. Use W, A, S, or D.")
                continue

            delta_r, delta_c = direction_map[move]
            new_r = player.pos_r + delta_r
            new_c = player.pos_c + delta_c

            # Verifica limites do tabuleiro
            if not (0 <= new_r < self.rows and 0 <= new_c < self.columns):
                print("Move out of bounds. Try another direction.")
                continue

            # Verifica se a nova célula está ocupada
            if not self.is_cell_free(new_r, new_c):
                print("Cell occupied by another player. Try another direction.")
                continue

            # Movimento válido: aplica
            player.pos_r = new_r
            player.pos_c = new_c

            self.update_grid()
            self.render_board()
