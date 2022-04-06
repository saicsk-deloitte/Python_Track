def multiply_twice(func):
    def inner(num1, num2):
        print("start")
        func(num1, num2)
        func(num1, num2)
        print("end")

    return inner
@multiply_twice
def multiply(n1, n2):
    print(n1 * n2)
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

multiply(a,b)