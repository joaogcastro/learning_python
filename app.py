from board import Board

board_columns = int(input('Insert board columns value: '))
board_rows = int(input('Insert board rows value: '))
board = Board(board_columns, board_rows)

while True:
    board.create_player()
    add_more = input('Do you want to add another player? (yes/no): ').strip().lower()
    if add_more not in ('yes', 'y'):
        break

while True:
    player_name = input('Who you want to move: ')
    board.move_player(player_name)

    move_other = input('You want to move another player? (yes/no): ').strip().lower()
    if add_more not in ('yes', 'y'):
        break

print('Thanks for playing ;)')
print('Bye !')