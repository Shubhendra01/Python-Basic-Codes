a = int(input('total classes held:'))
b = int(input('total classes attended:'))
c = (b/a*100)
print(c,'% attended')
if c < 75:
    print('student is not allowed to sit in exam')
else:
    print('student is allowed to sit in exam')
