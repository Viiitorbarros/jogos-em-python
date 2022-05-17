from random import randint
#VARIAVEIS
sort1 = sort2 = randint(1,6)
high = [8,9,10,11,12]
low= [2,3,4,5,6]
resultado = sort1 + sort2
r = 'S'
#PROGRAMA PRINCIPAL
print('ECOLHA UMA OPÇÃO!')
print('-> HIGH')
print('-> LOW')
print('-> 7')
deposito = float(input('DIGITE SUA BANCA:'))
while True:
    if deposito < 0:
        print('SEU DEPOSITO NAO PODE SER NEGATIVO:')
        deposito = float(input('DIGITE SUA BANCA:'))
    else:
        break
while True:
   if r == 'S':
    aposta = float(input('FAÇA SUA APOSTA:'))
    while True:
        if aposta > deposito:
            print('VOCÊ NÃO POSSUI SALDO PARA TAL APOSTA!')
            aposta = float(input('FAÇA SUA APOSTA:'))
        elif aposta < 0:
            print('A APOSTA NÃO PODE SER NEGATIVA!')
            aposta = float(input('FAÇA SUA APOSTA:'))
        else:
            break
    op= str(input('ESCOLHA UMA OPCÃO:')).upper()
    print('=-'*20)
    print(f'Primeiro dado = {sort1}\U0001f3b2')
    print(f'Segundo dado = {sort2} \U0001f3b2')
    print(f'Soma = {resultado}')
    print('=-'*20)
    if op == 'HIGH':
        if resultado in high:
            print('PARABÉNS VOCE VENCEU')
            print('VOCÊ GANHOU {:.0f}'.format(aposta*2))
            deposito =(deposito-aposta) + (aposta*2)
        else:
            print('VOCE PERDEU')
            deposito = deposito - aposta

    elif op == 'LOW':
        if resultado in low:
            print('PARABÉNS VOCE VENCEU')
            print('VOCÊ GANHOU {:.0f}'.format(aposta*2))
            deposito =(deposito-aposta) + (aposta*2)
        else:
            print('VOCE PERDEU')
            deposito = deposito - aposta
    elif op == '7':
        if resultado == 7:
            print('PARABÉNS VOCE VENCEU')
            print('VOCÊ GANHOU {:.0f}'.format(aposta*2.5))
            deposito = (deposito-aposta) + (aposta*2)
        else:
            print('VOCE PERDEU')
            deposito = deposito - aposta
    print('=-' * 20)
    print(f'SEU SALDO É DE : {deposito}')
    if deposito == 0:
        print('VOCÊ ZEROU SEU SALDO.', end='')
        r2= str(input('QUER ADIONAR MAIS SALDO ?[S/N]')).upper()
        if r2 == 'S':
            deposito = float(input('DIGITE SUA NOVA BANCA:'))

        else:
            print('SEU SALDO ZEROU. FIM DE GAME...')
            break

    r = str(input('QUER CONTINUAR [S/N]:')).upper()
    sort1 = sort2 = randint(1, 6)
    resultado = sort1 + sort2
   elif r == 'N':
       print('OBRIGADO POR APOSTAR!')
       break
   else:
       print('OPÇÃO INVALIDA!')
       r = str(input('QUER CONTINUAR [S/N]:')).upper()
