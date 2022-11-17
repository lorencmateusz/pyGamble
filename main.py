import random

MAX_LINES = 3
MAX_BET = 200
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

symbol_value = {
    'A': 5,
    'B': 2,
    'C': 3,
    'D': 4
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
    return winnings


def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_cnt in symbols.items():
        for _ in range(symbol_cnt):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns):
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input('How much would you like to deposit: ')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount should be greater than 0')
        else:
            print('Please input a valid number')
    return amount


def get_number_of_lines():
    while True:
        lines = input(f'Enter the number of lines between 1 and {MAX_LINES}: ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f'Enter the number of lines between 1 and {MAX_LINES}')
        else:
            print('Please input a valid number')
    return lines


def get_bet():
    while True:
        bet = input(f'Enter bet amount between {MIN_BET} and {MAX_BET}: ')
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f'Enter bet amount between {MIN_BET} and {MAX_BET}')
        else:
            print('Please input a valid number')
    return bet


def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines*bet
        if total_bet > balance:
            print(f"You don't have enough funds. Current balance: {balance}")
        else:
            break

    print(f'You are betting {bet}PLN on {lines} lines. Total bet is: {bet*lines}PLN')

    slots = get_spin(ROWS, COLS, symbol_count)
    print_machine(slots)
    winning = check_winnings(slots, lines, bet, symbol_value)
    print(f'You won {winning}')
    return winning - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Your balance: {balance}")
        choice = input('Press enter to play, press q to quit')
        if choice == 'q':
            break
        balance += game(balance)


main()



