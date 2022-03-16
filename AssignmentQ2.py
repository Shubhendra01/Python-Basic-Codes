a = input("enter the sentence: ").split()
b = {}
c = []
for i in a:
    b[i] = a.count(i)
for j in b:
    if b[j] == 1:
        c.append(j)
print(c)
