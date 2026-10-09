n = int(input("Введите число: ")) # Считываем число

simple = True # Считаем, что число простое

if n <= 1:
    simple = False # Числа 1 и меньше не простые
else:
    for i in range(2, n): # Проверяем делители от 2 до n-1  
        if n % i == 0:
            simple = False # Нашли делитель число не простое
            break

if simple:
    print("Y") # Число простое
else:
    print("N") # Число не простое