
n = int(input('Digite quantos asteriscos terá a base de sua pirâmide ? '))
cont = n - 1
cont2 = 1

for i in range(0, n):
    print(' ' * cont, '*' * cont2)
    cont = cont - 1
    cont2 = cont2 + 1