a = int(input('enter the marks:'))
if a <= 25:
    print('Grade F')
elif a >= 25 and a < 45:
    print('Grade E')
elif a >= 45 and a < 50:
    print('Grade D')
elif a >= 50 and a < 60:
    print('Grade C')
elif a >= 60 and a < 80:
    print('Grade B')
else:
    print('Grade A')
