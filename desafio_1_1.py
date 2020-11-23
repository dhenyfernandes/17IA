import numpy as np
import os


def is_prime(n):
    i = 2
    while(i < int(n/2)):
        if(n % i == 0):
            return False
        i += 1
    return True


def legendre_conjecture(n):
    resposta = []
    for x in range(n**2, (n+1)**2):
        if(is_prime(x)):
            resposta.append(x)
    return resposta


os.system('cls')
print('Bem vindo a Conjectura de Legendre\n')
while(True):
    numero = int(input('entre com um numero positivo (0 para sair) : '))
    if(numero == 0):
        print('\nFoi um prazer tê-lo conosco!\n')
        exit()
    if(numero < 0):
        print('\ntestamos apenas números positivos.\n')
        continue
    print(legendre_conjecture(numero))
