from random import randint
import time

print('--------- JOGO DA ADVINHAÇÃO 2.0---------')
print('OLÁ,VAMOS JOGAR!')
time.sleep(2)
print('ESTOU PENSANDO EM UM NÚMERO ENTRE 0 E 10')
print('TENTE ADVINHAR....')
print('-----------------------------------------')

n = int(input('Qual número eu pensei ?'))
sort = randint(0,10)#Sorteia um número.
cont = 1
while n != sort:
    if n > sort:
        print('Menos...')
        n = int(input('Tente Novamente:'))
        cont+=1
    elif n < sort:
        print('Mais...')
        n = int(input('Tente Novamente:'))
        cont += 1

print('PARABÉNS VOCÊ ACERTOU NA {}° TENTATIVA!!!'.format(cont))