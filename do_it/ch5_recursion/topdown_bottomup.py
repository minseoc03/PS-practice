#genuinely recursion
#recursive function w/ more than one caller in the function

def recur(n: int) -> int:
    if n > 0:
        recur(n-1) #first recursive call
        print(n)
        recur(n-2) #second recursive call

if __name__ == "__main__":
    x = int(input('Enter an integer: '))

    recur(x)

#top-down processing
"""
recur(4) calls recur(3)
recur(3) calls recur(2)
recur(2) calls recur(1)
recur(1) calls recur(0)
recur(0) does nothing so go back to caller
recur(1) prints 1 and calls recur(-1) #1
recur(-1) does nothing so go back to caller
recur(1) has done everything so go back to caller
recur(2) prints 2 and calls recur(0) #2
recur(0) does nothing so go back to caller
recur(2) has done everything so go back to caller
recur(3) prints 3 and calls recur(2) #3
recur(2) calls recur(1)
recur(1) calls recur(0) which does nothing
recur(1) prints 1 and calls recur(-1) which does nothing so go back to caller #1
recur(3) has done everthing so go back to caller
recur(4) prints 4 and calls recur(2) #4
recur(2) calls recur(1)
recur(1) calls recur(0)
recur(0) does nothing so go back to caller
recur(1) prints 1 and calls recur(-1) #1
recur(-1) does nothing so go back to caller
recur(1) has done everything so go back to caller
recur(2) prints 2 and calls recur(0) #2
recur(0) does nothing so go back to caller
recur(2) has done everything so go back to caller
recur(4) has done everything
program exit

1231412
"""

#bottom-up processing
"""
recur(1) calls recur(0) prints 1 and calls recur(-1)
because recur(0) and recur(-1) do nothing,
recur(1) prints 1

recur(2) calls recur(1) prints 2 and calls recur(0)
because recur(1) prints 1 and recur(0) does nothing,
recur(2) prints 1, prints 2

recur(3) calls recur(2), prints 3, and calls recur(1)
because recur(2) prints 1 and 2, and recur(1) prints 1,
recur(3) prints 1, 2, 3 and 1

recur(4) calls recur(3), prints 4, and calls recur(2)
because recur(3) prints 1,2,3,1 and recur(2) prints 1 and 2,
recur(4) prints 1,2,3,1,4,1,2
"""

#bottom-up processing goes over the recursive function more concisely without
#calling same function again like top-down processing called recur(1) and recur(2) over and over