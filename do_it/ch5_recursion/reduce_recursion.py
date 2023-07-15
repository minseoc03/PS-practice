def recur(n: int) -> int:
    if n > 0:
        recur(n-1) #first recursive call
        print(n)
        recur(n-2) #second recursive call / tail recursion

#remove tail recursion
def recur2(n: int) -> int:
    while n > 0:
        recur(n-1)
        print(n)
        n = n-2

#removing tail recurison is easy
#but it's difficult to remove all the recursion
#because original n value should be stored somewhere else
#so we can use stack to store the data
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from ch4_stack_queue.fixed_stack import FixedStack

def recur3(n: int) -> int:
    s = FixedStack(n)
    while True:
        if n > 0:
            s.push(n)
            n = n - 1
            continue
        if not s.is_empty():
            n = s.pop()
            print(n)
            n = n - 2
            continue
        
        break

if __name__ == "__main__":
    x = int(input('Enter an integer: '))
    recur3(x)