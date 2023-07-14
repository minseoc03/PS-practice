#Euclidean Algorithm
#Example below
"""
22 8 
8 6 <- smaller integer and remainder
6 2
2 0 <- if remainder becomes 0, stop the recursion
2
"""

#gcd function is also in math module
def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
    
if __name__ == "__main__":
    print('Loading...')
    print('GCD Calculator')
    x = int(input('Enter the first integer: '))
    y = int(input('Enter the second integer: '))

    print(f'GCD of entered two integers are {gcd(x,y)}')