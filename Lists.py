# Muhammad Khan --- Lists

a = [i*4 for i in range(0,11) ]
print(a)
b= []
for i in a:
    i=int(i/2)
    b.append(i)
print(b)
c = b[:]

for i in range(len(c)):
    temp = int(c[i]/2)
    c[i] = temp

print(c)
