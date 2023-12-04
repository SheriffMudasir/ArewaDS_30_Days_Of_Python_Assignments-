numbers = [1, 1, 1, 1, 1, 2, 1, 2, 4, 8, 3, 1, 3, 9, 27, 4, 1, 4, 16, 64, 5, 1, 5, 25, 125]
row = 5
column = 5
for i in range(row):
    for j in range(column):
        index = i * column + j
        print(f"{numbers[index]:<3}", end="")
    print()
