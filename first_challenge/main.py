from time import sleep

DAILY_WITHDRAWAL_LIMIT = 3
MAX_WITHDRAWAL_LIMIT = 500

extract = []
balance = 0
withdrawal = 0
withdrawal_count = 0
deposit = 0

print("Welcome to the ATM")

menu = '''
    Select an option:
    1. Withdrawal
    2. Deposit
    3. Check Balance
    4. Exit
'''

while True:
    sleep(2)
    print(menu)
    option = input("Enter your option: ")

    if option == '1':
        withdrawal = float(input("Enter the amount you want to withdraw: "))
        if withdrawal >= MAX_WITHDRAWAL_LIMIT:
            print("You cannot withdraw more than 500")
        elif withdrawal > balance:
            print("Insufficient balance")
        elif withdrawal_count >= DAILY_WITHDRAWAL_LIMIT:
            print("You have reached the daily withdrawal limit")
        else:
            balance -= withdrawal
            withdrawal_count += 1
            extract.append(f'Withdrawal: {withdrawal:.2f}')
            print(f'You have withdrawn {withdrawal:.2f}')
        continue
    if option == '2':
        deposit = float(input("Enter the amount you want to deposit: "))
        balance += deposit
        extract.append(f'Deposit: {deposit:.2f}')
        print(f'You have deposited {deposit:.2f}')
        continue
    if option == '3':
        print('This is your extract:\n')
        print('#' * 20)
        if extract.__len__() == 0:
            print('No operations have been made')
        else:
            for operation in extract:
                print(operation)
        print(f'\nYour balance is {balance:.2f}')
        print('#' * 20)
        continue
    if option == '4':
        print('Thank you for using the ATM')
        break
    else:
        print('Invalid option')
        continue
