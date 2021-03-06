h = float (input('Введите шаг: '))
eps = float (input('Введите точность: '))
N = int (input('Введите максимальное число итераций: '))

# Запускаем секундомер
twork = time.clock()

# Код ошибки
print('''
Код ошибки:
0 - нет ошибок
1 - превышено количество итераций
''')

# Заголовок таблицы
print('''
|---------|---------|---------|-------------|---------------|-----------|--------|
| №       |         |         |             |               | Число     | Код    |
| корня   |  X(n)   |  X(n+1) |     X       |     f(X)      | итераций  | ошибки |
|---------|---------|---------|-------------|---------------|-----------|--------| ''')

# Базовые параметры
i = 0
Xn = a
Xn1 = a + h

while Xn1 < b + h:
    # Найден корень в отрезке
    if f(Xn) * f(Xn1) <= 0:
        # Начальные значения для метода хорд (temp - неподвижная точка)
        if ddf((Xn + Xn1)/2) < 0:
            temp = Xn
            X1 = Xn1
        else:
            temp = Xn1
            X1 = Xn
        # Начальные значения для метода касательных
        if df(Xn) > 0:
            X_1 = Xn
        else:
            X_1 = Xn1
            
        code = 0
        i += 1
        n = 0
        # Начало итераций
        while True:
            n += 1
            X2 = X1 - (f(X1) * (X1 - temp))/(f(X1) - f(temp))
            if abs(X2 - X1) <= eps:
                break
            X_2 = X_1 - f(X_1) / df(X_1)
            X1 = X_2
            X_1 = X_2
            
            # Проверка на MAX итераций
            if n == N:
                code = 1
                break
            
        # Значение корня
        X = (X1 + X2)/2
        
        # Табличный вывод
        if code == 0:
            #         №           Xn         Xn+1      X        f(X)     Итерации         Код
            print("|{:3d}      |{:7.2f}  |{:7.2f}  |{:11.6f}  |{:11.2e}    |{:4d}       |{:3d}     |"\
                .format(i, Xn, Xn1, X, f(X), n, code))
        elif code == 1:
            print("|{:3d}      |{:7.2f}  |{:7.2f}  |   ---       |     ---       |{:4d}       |{:3d}     |"\
                .format(i, Xn, Xn1, n, code))
                             
    Xn = Xn1
    Xn1 += h
    
time = time.clock() - twork
print("\nВремя выполнения программы = {:8.4f}".format(time))
       
#________________________________Конец кода( ~ 110 строк )_____________
