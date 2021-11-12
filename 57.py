n = int(input())
if n % 5 == 0 and n % 7 == 0:
    print('00')
elif n % 5 == 0 and n % 7 != 0:
    print('01')
elif n % 5 != 0 and n % 7 == 0:
    print('10')
else:
    print('11')