#8queen problem
#placing queen on the chess board, making queens can't catch each other

#branching
#juxtapositioning all the combinations like branch

#divide and conquer
#dividing problem into smaller problem and derive a solution to an original problem

#in this file
#making sure that no queen can be placed at the same column

#i -> col (index)
#j -> row (value)
pos = [0] * 8

def put() -> None:
    for i in range(8):
        print(f'{pos[i]:2}', end = '')
    print()

def set(i: int) -> None:
    for j in range(8):
        pos[i] = j
        if i == 7:
            put()
        else:
            set(i + 1)

if __name__ == "__main__":
    set(0)

#add another rule
#queens can't be placed at same row
pos1 = [0] * 8
#bounding
#removing unnecessary branch
flag1 = [False] * 8

def put1() -> None:
    for i in range(8):
        print(f"{pos[i]:2}", end = '')
    print()

def set1(i: int) -> None:
    for j in range(8):
        if not flag1[j]:
            pos[i] = j
            if i == 7:
                put1()
            else:
                flag1[j] = True
                set1(i+1)
                #reset chess board for next case
                flag1[j] = False
set1(0)

#add another rule
#queens can't be placed at same diagonal line

pos2 = [0] * 8
flag_a = [False] * 8 #for checking row
flag_b = [False] * 15 #for checking right diagonal
flag_c = [False] * 15 #for checking left diagonal

def put2() -> None:
    for i in range(8):
        print(f'{pos2[i]:2}', end = '')
    print()

def set2(i: int) -> None:
    for j in range(8):
        if (not flag_a[j]
            and not flag_b[i+j]
            and not flag_c[i-j+7]):
            pos2[i] = j
            if i == 7:
                put2()
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = True
                set2(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = False

set2(0)