from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    #O(1)
    pl = 0
    #O(1)
    pr = len(a) - 1

    while True:
        #O(log n)
        pc = (pl + pr) // 2
        #O(log n)
        if a[pc] == key:
            #O(1)
            return pc
        #O(log n)
        elif a[pc] < key:
            #O(log n)
            pl = pc + 1
        else:
            #O(log n)
            pr = pc - 1
        #O(log n)
        if pl > pr:
            break
    #O(1)
    return -1

    #TIME COMPLEXITY -> O(log n)

if __name__ == "__main__":
    num = int(input("Enter the number of elements: "))
    x = [None] * num

    print("Enter the elements in ascending order")

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        #make sure user enter elements in ascending order by using infinite loop
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i-1]:
                break

    ky = int(input("Enter the element to search: "))

    idx = bin_search(x, ky)

    if idx == -1 :
        print("Following element does not exist in this sequence")
    else:
        print(f"Following element is at x[{idx}]")