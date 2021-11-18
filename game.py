import random 

real_num = random.randint(1, 100)

k = int(input('input a number of attemts: '))

print(real_num, 'хаха обыграй ка комьютер!')

attempt = int(input())

while k > 1:

    if attempt < real_num:

        print('too low')

        k -= 1

        attempt = int(input())

    if attempt > real_num:

        print('too big')

        k -= 1

        attempt = int(input())

    elif attempt == real_num:

        print('you won')

        break

else:
    print('you lose')


        


        


