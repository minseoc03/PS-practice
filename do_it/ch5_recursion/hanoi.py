def move(no: int, x: int, y: int) -> None:
    if no > 1:
        move(no - 1, x, 6 - x - y)
    
    print(f'Moving Plates No.{no} from {x} to {y}')

    if no > 1:
        move(no - 1, 6 - x - y , y)

if __name__ == "__main__":
    print("Generating Tower of Hanoi")
    n = int(input('Enter the number of plates: '))

    move(n, 1, 3)

"""
3 1 3
2 1 2
1 1 3 (Printed)
2 1 2 (Printed)
1 3 2 (Printed)
3 1 3 (Printed)
2 2 3
1 2 1 (Printed)
2 2 3 (Printed)
1 1 3 (Printed)
"""