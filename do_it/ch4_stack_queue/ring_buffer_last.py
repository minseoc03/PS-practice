#ring buffer can be used to remove old data

n = int(input('How many data would be stored?: '))
a = [None] * n

cnt = 0
while True:
    a[cnt % n] = int(input(f'Enter {cnt+1}th data: '))
    cnt += 1

    retry = input(f'Continue? (Y ... Yes / N ... No): ')
    if retry in ['N', 'n']:
        break

i = cnt - n
if i < 0: i = 0

while i < cnt:
    print(f'{i + 1}th = {a[i % n]}')
    i += 1