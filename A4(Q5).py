num = int(input('enter the integer:'))
if num > 0:
    for i in range(2,num):
        if(num % i) == 0:
            print(num, 'it is not a prime number')
            break
        else:
            print(num, 'it is a prime number')
            break
