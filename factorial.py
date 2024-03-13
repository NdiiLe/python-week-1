def factorial (x):
    if x == 1:
        return 1
    
    else:
        return (x * factorial(x-1))
    
    number = int(input("enter a number:"))
    
    result = factorial(number)
    
    print("the factorial of", number, "is", result)
    
    
    
    
    # Python code to demonstrate naive method
# to compute factorial
number = 23
fact = 1

for i in range(1, number+1):
	fact = fact * i

print("The factorial of 23 is : ", end="")
print(fact)
