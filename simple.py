n = int(input("Введите число: "))

simple = True

if n <= 1:
    simple = False
else:
    for i in range(2, n):
        if n % i == 0:
            simple = False
            break

if simple:
    print("Y")
else:
    print("N")