import random


def run():
    WIN_LINES = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6))
    new_game = True

    print("Игра «Крестики-нолики»")
    print("Клетки пронумерованы от 1 до 9.")

    while new_game:
        # Кто ходит первым
        print(
'''
Кто ходит первым?
1. Игрок
2. Система
3. Случайно
''')
        while 1:
            first = input("Ваш выбор (1-3): ").strip()
            if first in ('1', '2', '3'):
                break
            print("Нужно ввести 1, 2 или 3. Попробуйте снова.")

        if first == '3':
            first = random.choice(('1', '2'))
            if first == '1':
                print("Случайный выбор: первым ходит игрок.")
            else:
                print("Случайный выбор: первой ходит система.")

        if first == '1':
            player_turn = True
            player_mark = 'X'
            system_mark = 'O'
        else:
            player_turn = False
            player_mark = 'O'
            system_mark = 'X'

        print(f"\nВы играете за {player_mark}, система играет за {system_mark}. "
              f"Первым ходит X.\n")

        board = [' '] * 9
        moves = 0
        result = None  # None, player, system или draw

        while 1:
            # Вывод поля
            for row in range(3):
                cells = []
                for col in range(3):
                    cell = board[row * 3 + col]
                    if cell == ' ':
                        cell = str(row * 3 + col + 1)
                    cells.append(cell)
                print(' ' + ' | '.join(cells))
                if row < 2:
                    print('---+---+---')
            print()

            if result is not None:
                break

            if player_turn:
                # Ход игрока
                while 1:
                    move_str = input("Ваш ход (1-9): ").strip()
                    if move_str not in tuple('123456789'):
                        print("Нужно ввести число от 1 до 9. Попробуйте снова.")
                        continue
                    index = int(move_str) - 1
                    if board[index] != ' ':
                        print("Эта клетка занята. Выберите другую.")
                        continue
                    break
                board[index] = player_mark
            else:
                # Ход системы это случайная свободная клетка
                free = [i for i in range(9) if board[i] == ' ']
                move = random.choice(free)
                board[move] = system_mark
                print(f"Система ходит в клетку {move + 1}.\n")

            moves += 1

            # Проверка победы или не победы
            for line in WIN_LINES:
                a, b, c = line
                if board[a] != ' ' and board[a] == board[b] == board[c]:
                    if board[a] == player_mark:
                        result = 'player'
                    else:
                        result = 'system'
            if result is None and moves == 9:
                result = 'draw'

            player_turn = not player_turn

  
        if result == 'player':
            print("Поздравляю! Вы победили!")