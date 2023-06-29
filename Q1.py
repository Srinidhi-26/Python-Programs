
for num in range(3, 100, 10):
    if num % 10 ==3:
        prime =True
        for i in range(2,int(num** 0.5)+1):
            if num % i == 0:
                prime = False
                break
        if prime:
            print(num)