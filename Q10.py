def pattern(rows):
    for i in range(1, rows+1):
        for j in range(1, i+1):
            print("*", end="")
        print()

rows = int(input("enter how many rows"))
pattern(rows)