a = ['my','name','','is']
b = []
i = 0
while i < len(a):
    if a[i] != "":
        b.append(a[i])
    i += 1
print(b)
