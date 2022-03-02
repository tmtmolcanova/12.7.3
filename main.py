# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
money = int(input("Enter sum: "))

#Имеем словарь со значениями процентных ставок в банках
# Объявляем депозиты в список

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []

for value in per_cent.values():
   result = int(money / 100 * value)
   deposit.append(result)
print(deposit)
print("Максимальная сумма, которую вы можете заработать:",max(deposit))
