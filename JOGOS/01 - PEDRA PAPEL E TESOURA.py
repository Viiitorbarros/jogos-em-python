from random import randint
import time

print('===========PEDRA PAPEL E TESOURA===========')

print('[1] PEDRA \u26F0')
print('[2] PAPEL \U0001f9fb')
print('[3] TESOURA \u2702')
itens = ('PEDRA' , 'PAPEL', 'TESOURA')
computador = randint(0,2)
jogador = int(input('ESCOLHA UMA OPÇÃO:'))
print('==============================================')
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('POOO!!!')
print('==============================================')
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador-1]))
if computador == 0: # PEDRA
    if jogador -1 == 0:
        print('VOCÊS EMPATARAM \U0001F612!!!')
    elif jogador - 1 == 1:
        print('PARABÉNS JOGADOR, VOCE VENCEU \U0001F973!!!')
    elif jogador - 1 == 2:
        print('O COMPUTADOR VENCEU \U0001F614 !!!')
    else:
        print('JOGADA INVALIDA')
if computador == 1: # PAPEL
    if jogador -1 == 0:
        print('O COMPUTADOR VENCEU \U0001F614 !!!')
    elif jogador - 1 == 1:
        print('VOCÊS EMPATARAM \U0001F612!!!')
    elif jogador -1 == 2 :
        print('PARABÉNS JOGADOR, VOCE VENCEU \U0001F973!!!')
    else:
        print('JOGADA INVALIDA')
if computador == 2: #TESOURA
    if jogador -1 == 0:
        print('PARABÉNS JOGADOR, VOCE VENCEU \U0001F973!!!')
    elif jogador - 1 == 1:
        print('O COMPUTADOR VENCEU \U0001F614 !!!')
    elif jogador - 1 == 2:
        print('VOCÊS EMPATARAM \U0001F612!!!')
    else:
        print('JOGADA INVALIDA')