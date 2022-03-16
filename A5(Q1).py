a = input("enter the sentence: ").split()
b = {}
for i in a:
    b[i] = a.count(i)
for j in b:
    print(j, ':', b[j])
