from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu', ['Push', 'Pop', 'Peek', 'Search', 'Dump', 'Exit'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '   ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)
        
s = FixedStack(64)

while True:
    print(f'Current Number of Data: {len(s)} / {s.capacity}')
    menu = select_menu()

    if menu == Menu.Push:
        x = int(input('Enter the data: '))
        try:
            s.push(x)
        except FixedStack.Full:
            print('The stack is full')
    
    elif menu == Menu.Pop:
        try:
            x = s.pop()
            print(f'Popped data is {x}')
        except FixedStack.Empty:
            print('The stack is empty')

    elif menu == Menu.Peek:
        try:
            x = s.peek()
            print(f'Peeked data is {x}')
        except FixedStack.Empty:
            print('The stack is empty')
    
    elif menu == Menu.Search:
        x = int(input('Enter the data to search: '))
        if x in s:
            print(f'There are {s.count(x)} data in this stack, and the most front one is at {s.find(x)}')
        else:
            print("Unable to find desired data")
        
    elif menu == Menu.Dump:
        s.dump()
    
    else:
        break