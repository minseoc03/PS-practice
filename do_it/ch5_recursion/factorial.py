#direct recursion
#calling myself inside the corresponding function
#ex) factorial

#indirect recursion
#ex) b() calls a() calls b() ... 

#factorial can be calculated by using math module
#this example is used for demonstrating recursive function
#not useful 

def factorial(n: int) -> int:
    if n > 0:
        return n * factorial(n - 1)
    
    else:
        return 1
    
if __name__ == '__main__':
    n = int(input('Enter the number: '))
    print(f'The factorial of {n} is {factorial(n)}')