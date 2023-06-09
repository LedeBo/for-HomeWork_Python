# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no


print("Введите шестизначный номер билета: ")
tnumber = input()
if len(tnumber) != 6:
    print("Вы ввели не шестизначное число, билет с таким номером не подойдет")
else:
    suml = int(tnumber[0]) + int(tnumber[1]) + int(tnumber[2])
    sumr = int(tnumber[3]) + int(tnumber[4]) + int(tnumber[5])
    if suml == sumr:
        print("YES -> Ура! Ваш билетик счастливый!")
    else:
        print("NO -> В этот раз Вам попался обычный билетик.")
