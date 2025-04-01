number = int(input("enter a number: "))
def factorial(number):
    if number<2:
        return 1
    else:
        return number*factorial(number-1)
result = factorial(5)
print("factorial of 5 is ",result)
