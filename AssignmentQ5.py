a=input("enter the sentence: ")
b=a.split(' ')
c=b[0]
for i in b:
    if len(i) > len(c):
        c=i
print('Largest word:',c)
if len(i) < len(c):
        c=i
print('smallest word:',c)
