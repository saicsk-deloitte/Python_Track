n=int(input("enter no of rows:" ))
for i in range(1,n+1):
    a= 1
    for j in range(1, i + 1):
        print(' ', a, sep='', end='')
        a = a * (i - j) // j
    for j in range(0,n-i):
     print(' 0', end='')
    print()

