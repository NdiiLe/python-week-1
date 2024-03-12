def factorial (x):
    if x == 1:
        return 1
    
    else:
        return (x * factorial(x-1))
    
    number = int(input("enter a number:"))
    
    result = factorial(number)
    
    print("the factorial of", number, "is", result)