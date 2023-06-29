def maximum(a,b,c):
    max_ =a

    if b> max_:
        max_ = b

    if c > max_:
        max_ = c 
    
    print(max_)

num1 = int(input('enter num1:'))
num2 = int(input('enter num2:'))
num3 = int(input('enter num3:'))

v = maximum(num1, num2, num3)