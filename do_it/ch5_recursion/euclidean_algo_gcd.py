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