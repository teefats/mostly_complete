# Python Program to find Factorial of a Number

# number = int(input(" Please enter any Number to find factorial : "))
def factorial(x=int):
    # try:
    
        
    if x >= 0:
        
        factorial = 1

        for i in range(1, x + 1):
            factorial = float(factorial * i)
        print(f' The factorial of {x} is {factorial}') 
        return factorial

    else:
        raise ValueError("Sorry x cannot be a negative number")
    
    

    # except number < 0:
    #     raise ValueError

factorial(3)