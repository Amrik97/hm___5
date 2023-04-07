def power(num, pw, i, res):
    if i == pw:
        print("A = " + str(num) + "; B = " + str(pw) + " -> " + str(res))
        return
    i += 1
    res *= num
    power(num, pw, i, res)


if __name__ == '__main__':
    print("Введите натуральное число которое нужно возвести в степень: ")
    try:
        num = int(input())
    except ValueError:
        print("Вы ввели не целое число!")
        exit()
    print("Введите степень числа: ")
    try:
        pw = int(input())
    except ValueError:
        print("Вы ввели не целое число!")
        exit()
    if num == 0:
        print("A = " + str(num) + "; B = " + str(pw) + " -> " + str(0))
        exit()
    elif pw == 0:
        print("A = " + str(num) + "; B = " + str(pw) + " -> " + str(1))
        exit()
    elif pw == 1:
        print("A = " + str(num) + "; B = " + str(pw) + " -> " + str(num))
        exit()
    power(num, pw, 1, num)