a = input('enter the string:')
low = a.lower()
vowels = {}
for i in "aeiou":
    b = low.count(i)
    vowels[i] = b
print(vowels)
