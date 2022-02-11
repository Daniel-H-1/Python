base = int (input ('Digite o valor de base'))
expoente = int (input ('Digite o valor de expoente'))

cont = 0
produto = 1

while cont < expoente:
    produto = produto*base
    cont = cont + 1

print(base,'elevado a' ,expoente, '=',produto)
