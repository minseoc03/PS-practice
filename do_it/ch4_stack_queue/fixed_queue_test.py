from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Menu', ['Enque', 'Deque', 'Peek', 'Search', 'Dump', 'Exit'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '   ', end = '')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)
        
q = FixedQueue(64)

while True:
    print(f'Current Data Number: {len(q)} / {q.capacity}')
    menu = select_menu()

    if menu == Menu.Enque:
        x = int(input('Enter the data to enque: '))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print('The queue is full')
        
    elif menu == Menu.Deque:
        try:
            x = q.deque()
            print(f'{x} is dequed')
        except FixedQueue.Empty:
            print('The queue is empty')
    
    elif menu == Menu.Peek:
        try:
            x = q.peek()
            print(f'Peek data is {x}')
        except FixedQueue.Empty:
            print('The queue is empty')
    
    elif menu == Menu.Search:
        x = int(input('Enter the data to search: '))
        if x in q:
            print(f'There are {q.count(x)} data in queue and the foremost one is at {q.find(x)}')
        else:
            print('Unable to find desired data')
    
    elif menu == Menu.Dump:
        q.dump()
    
    else:
        break
