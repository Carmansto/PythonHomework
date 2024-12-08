from random import randint
from datetime import date

def stepFunc(a,b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    return a * stepFunc(a,b-1)

def sumFunc(a,b):
    if a > b:
        return 0
    return a+sumFunc(a+1, b)

def starFunc(n):
    if n <= 0:
        return
    print('*', end='')
    starFunc(n - 1)

def find_min_sum_sequence(num_list):
    min_index = 0
    min_sum = sum(num_list[:10])

    for i in range(1, len(num_list) - 9):
        current_sum = sum(num_list[i:i + 10])
        if current_sum < min_sum:
            min_sum = current_sum
            min_index = i

    return min_index, min_sum

def is_vus_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_between_dates(year1, month1, day1, year2, month2, day2):
    date1 = date(year1, month1, day1)
    date2 = date(year2, month2, day2)
    sum_days = abs((date2 - date1).days)
    return sum_days


print("---Завдання 1---")
print(stepFunc(3,2))

print("---Завдання 2---")
print(sumFunc(1,5))

print("---Завдання 3---")
starFunc(5)
print("")

print("---Завдання 5---")
random_list = [randint(0, 1000) for _ in range(100)]
pos, minimum_sum = find_min_sum_sequence(random_list)

print(f"Позиція початку послідовності: {pos}")
print(f"Сума на цій позиції: {minimum_sum}")
print(f"Послідовність: {random_list[pos:pos + 10]}")

print("---Завдання 6---")
day1, month1, year1 = 1, 1, 2024
day2, month2, year2 = 1, 1, 2025
print(f"Різниця між датами {day1}.{month1}.{year1} та {day2}.{month2}.{year2}: {days_between_dates(year1, month1, day1, year2, month2, day2)} днів")
print(f"2024 високосний: {is_vus_year(2024)}")
print(f"2025 високосний: {is_vus_year(2025)}")

print("---Завдання 4---")
def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def display_board(board):
    for row in board:
        for i in range(len(row)):
            if i < len(row) - 1:
                print(row[i], end="|")
            else:
                print(row[i])
        print("-" * 5)


def check_winner(board, player):
    for row in board: # Перевірка рядків
        all_match = True
        for cell in row:
            if cell != player:
                all_match = False
                break
        if all_match:
            return True


    for col in range(3): # Перевірка колонок
        all_match = True
        for row in range(3):
            if board[row][col] != player:
                all_match = False
                break
        if all_match:
            return True


    all_match = True # Перевірка діагоналей
    for i in range(3):
        if board[i][i] != player:
            all_match = False
            break
    if all_match:
        return True

    all_match = True
    for i in range(3):
        if board[i][2 - i] != player:
            all_match = False
            break
    if all_match:
        return True

    return False

# Перевірка на нічию
def check_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def position_to_coordinates(position):
    mapping = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }
    return mapping.get(position)


def player_move(board, player):
    while True:
        try:
            move = int(input(f"Гравець {player}, введіть клітинку для ходу(1-9):  "))
            if move < 1 or move > 9:
                print("Від 1 до 9!")
                continue

            row, col = position_to_coordinates(move)
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Ця клітинка вже зайнята. Спробуйте іншу.")
        except (ValueError, TypeError):
            print("Від 1 до 9!")


def play_game():
    board = create_board()
    current_player = "X"

    print("Введіть число від 1 до 9 для вибору клітинки:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")

    while True:
        player_move(board, current_player)
        display_board(board)

        if check_winner(board, current_player):
            print(f"Гравець {current_player} переміг!")
            break
        elif check_draw(board):
            print("Нічия!")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()
