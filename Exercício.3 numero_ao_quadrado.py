'''
Dada uma sequência de números inteiros não-nulos,
seguida por 0, imprimir seus quadrados.
'''

n = int (input('digite o valor de n: '))

while n != 0:
    print(n,'ao quadrado =', n*n)
    n = int (input('Digite o proximo número: '))
