# Задача 3: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

print("Введите номер билета:")
num = int(input())

if num > 999999: # Проверка номера. Номер не может содержать больше 6 цифр. Меньше 6 -> первые числа - нули
    print("Ошибка ввода")
    exit()

left_side = num // 1000
right_side = num % 1000

left_side_sum = left_side // 100 + left_side // 10 % 10 + left_side % 10 % 10
right_side_sum = right_side // 100 + right_side // 10 % 10 + right_side % 10 % 10

if left_side_sum == right_side_sum:
    print(num, "-> yes")
else:
    print(num, "-> no")