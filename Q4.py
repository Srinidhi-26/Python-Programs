def sec_highest(num):
    max_ = 0
    sec_max = 0
    for n in num:
        if n >max_:
            sec_max = max_
            max_ = n
        elif n > sec_max and n != max_:
            sec_max= n
    
    print(sec_max)


list1 = [1,2,3,4,5,6]
v = sec_highest(list1)
