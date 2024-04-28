from time import sleep

DAILY_WITHDRAWAL_LIMIT = 3
MAX_WITHDRAWAL_LIMIT = 500

extract = []
balance = 0
withdrawal_count = 0

print("Welcome to the ATM")

menu = '''
    Select an option:
    1. Withdrawal
    2. Deposit
    3. Check Balance
    4. Exit
'''


def withdrawal(balance, withdrawal_count, DAILY_WITHDRAWAL_LIMIT, MAX_WITHDRAWAL_LIMIT, extract):
    withdrawal_value = float(input("Enter the amount you want to withdraw: "))
    if withdrawal_value >= MAX_WITHDRAWAL_LIMIT:
        print("You cannot withdraw more than 500")
    elif withdrawal_value > balance:
        print("Insufficient balance")
    elif withdrawal_count >= DAILY_WITHDRAWAL_LIMIT:
        print("You have reached the daily withdrawal limit")
    else:
        balance -= withdrawal_value
        withdrawal_count += 1
        extract.append(f'Withdrawal: {withdrawal_value:.2f}')
        print(f'You have withdrawn {withdrawal_value:.2f}')
    return balance, withdrawal_count


def deposit(balance, extract):
    deposit_value = float(input("Enter the amount you want to deposit: "))
    balance += deposit_value
    extract.append(f'Deposit: {deposit_value:.2f}')
    print(f'You have deposited {deposit_value:.2f}')
    return balance


def extract_view(extract, balance):
    print('This is your extract:\n')
    print('#' * 20)
    if extract.__len__() == 0:
        print('No operations have been made')
    else:
        for operation in extract:
            print(operation)
    print(f'\nYour balance is {balance:.2f}')
    print('#' * 20)


while True:
    sleep(2)
    print(menu)
    option = input("Enter your option: ")

    if option == '1':
        balance, withdrawal_count = withdrawal(
            balance,
            withdrawal_count,
            DAILY_WITHDRAWAL_LIMIT,
            MAX_WITHDRAWAL_LIMIT,
            extract)
        continue
    if option == '2':
        balance = deposit(balance, extract)
        continue
    if option == '3':
        extract_view(extract, balance)
        continue
    if option == '4':
        print('Thank you for using the ATM')
        break
    else:
        print('Invalid option')
        continue
