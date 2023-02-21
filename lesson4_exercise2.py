# ____________________Примечание________________________
# конвертируем кодировку файла в UTF-8, иначе компилятор 
# ругается что кодек не может прочитать русские символы 

print("__________________Урок_4,_задание_2__________________")
print("Программа разбития пятизначного числа на цыфры и выполнение")
print("математических операций с цыфрами исходного числа")

# чтобы программа не закрывалась сразу после вывода результата
# создаём переменную-флаг выхода из программы

exit = 1

# создаём цыкл программы с условием для выхода из программы

while exit == 1:
    
    # вводим пятизначное исходное число

    print()
    print("______________Введите_пятизначное_число______________")

    cheslo = input()

    # проверяем чтобы число было пятизначным

    if len(cheslo)!=5: 

        print("Введённое число не пятизначное") 

    else:

    # разбиваем исходное число на цыфры

        edenici = int(cheslo[4])

        desatci = int(cheslo[3])

        sotni = int(cheslo[2])

        tisachi = int(cheslo[1])

        des_tisach = int(cheslo[0])
        
    # возводим количество десятков в степень количества единиц

        stepen = desatci ** edenici

    # умножаем предыдущую степень на количество сотен

        proizvedenie = stepen * sotni

    # делим получившееся число на разность количества десятков тысяч и количества тысяч

        chasnoe = proizvedenie / (des_tisach - tisachi)

        print()
        print("Ответ равен " + str(chasnoe))

    # далее либо выполняем ещё цикл вычисления, либо выходим из программы

    print()
    print("----------------------------------------------")
    print("Чтобы выполнить ещё расчёт, введите число 1.")
    print("Чтобы выйти из программы, введите число 0.")

    exit=int(input())

