def fibonacci(n):
    first=0
    second=1
    while(n>0):
        sum=first+second
        first=second
        second=sum
        yield sum
        n-=1
n=int(input("enter values of n:"))
print("0 \n1")
value=fibonacci(n)
for i in value:
    print(i)
