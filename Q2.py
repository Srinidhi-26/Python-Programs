def fib(n):
    series=[0,1]
    while series[-1] + series[-2] <=n:
        series.append(series[-1] + series[-2])
    print(series)

num =int(input('enter the number'))
fibna = fib(num)
