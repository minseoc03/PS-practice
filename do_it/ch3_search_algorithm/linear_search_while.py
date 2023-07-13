from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    #O(1)
    i = 0

    #O(n)
    while True:
        #O(n)
        if i == len(a):
            #O(1)
            return -1
        #O(n)
        if a[i] == key:
            #O(1)
            return i
        #O(n)
        i += 1
    
    #TIME COMPLEXITY -> O(n)

if __name__ == '__main__':
    num = int(input("Enter the number of element: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input("Enter the number you want to search: "))

    idx = seq_search(x, ky)

    if idx == -1:
        print("Key does not exist in following sequence")
    else:
        print(f"Following element is at x[{idx}]")
