n = eval(input("Enter diamond's height: "))
for x in range(n):
    print(" " * (n - x), "*" * (2*x + 1))
for x in range(n - 2, -1, -1):
    print(" " * (n - x), "*" * (2*x + 1))

    ###########################################################
rows = int(input("Enter no of required Rows = "))
for i in range(rows):
    for j in range(0, rows - i):
        print(' ', end = '')
    for k in range(0, i):
         print('*', end = '')
    print()

for i in range(rows, 0, -1):
    for j in range(0, rows - i):
        print(' ', end = '')
    for k in range(0, i):
         print('*', end = '')
    print()


