def counter(num, even, odd):
    if num == 0:
        print("Количество четных и нечетных цифр в числе равно: " + "(" + str(even) + "," + str(odd) + ")")
        return
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10
    counter(num, even, odd)


if __name__ == '__main__':
    print("Введите число: ")
    num = int(input())
    even, odd = 0, 0
    counter(num, even, odd)