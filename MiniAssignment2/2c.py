n= int(input("enter no of rows:"))
for row in range(1,n+1):
    for col in range(1,n+1):
        if(col == n) or (row == 1) or (col == row):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()