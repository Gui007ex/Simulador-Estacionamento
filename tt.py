total = []
par, impar = [],[] 

for n in range(1,361):
    if 360%n == 0:
        total.append(n)
        if n%2 == 0:
            par.append(n)
        else:
            impar.append(n)

print(len(total), len(par), len(impar))

print(total)