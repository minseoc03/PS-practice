from enum import Enum
from open_hash import OpenHash

Menu = Enum('Menu', ['Add', 'Delete', 'Search', 'Dump', 'Exit'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '    ', end = '')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)
        
hash = OpenHash(13)

while True:
    menu = select_menu()

    if menu == Menu.Add:
        key = int(input('Enter a key to add: '))
        val = input('Enter a value to add: ')
        if not hash.add(key, val):
            print('Failed to add.')
    
    elif menu == Menu.Delete:
        key = int(input('Enter a key to delete: '))
        if not hash.remove(key):
            print('Failed to delete.')
    
    elif menu == Menu.Search:
        key = int(input('Enter a key to search: '))
        t = hash.search(key)
        if t is not None:
            print(f'Value with searched key is {t}')
        else:
            print('There is no data to search')

    elif menu == Menu.Dump:
        hash.dump()
    
    else:
        break