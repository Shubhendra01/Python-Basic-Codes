a = input('enter the age a:')
b = input('enter the age b:')
c = input('enter the age c:')
if a > b and a > c:
    print('A is the oldest person')
elif b > a and b > c:
    print('B is the oldest person')
else:
    print('C is the oldest person')
if a < b and a < c:
    print('A is the youngest person')
elif b < a and b < c:
    print('B is the youngest person')
else:
    print('C is the youngest person')
