a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
d = (b ** 2) - 4 * a * c 
x1 = (-b + (d ** 0.5)) / 2 * a 
x2 = (-b - (d ** 0.5)) / 2 * a 

print('корни: ', x1, x2)