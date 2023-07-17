#sentinel method
#Original linear search requires two condition checks
# 1 Check whether key is found
# 2 Check whether search has reached the end of sequence
#Sentinel method reduces two condition checks to one by creating sentinel (key) at the end of the sequence

from typing import Any, Sequence
import copy
import time

def seq_search(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq)
    a.append(key)

    i = 0

    while True:
        #only used one if statement in while loop
        if a[i] == key:
            break
        i += 1
    
    return -1 if i == len(seq) else i

if __name__ == '__main__':
    num = int(input("Enter the number of element: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input("Enter the number you want to search: "))

    start = time.time()

    idx = seq_search(x, ky)

    if idx == -1:
        print("Key does not exist in following sequence")
    else:
        print(f"Following element is at x[{idx}]")

    end = time.time()

    print(f"It took {end - start:.5f} sec to search element")