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


def main():
    balance = deposit()
