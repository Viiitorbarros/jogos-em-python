from random import randint

############## NOME ##########
print('-=-'*10)
print('Bem vindo ao Game de advinhação.')
print('-=-'*10)
############## DIFICULDADE DO GAME ##########
print('Nivel de Dificuldade:')
print('[1] Facil')
print('[2] Médio')
print('[3] Dificil')

while True :

    nivel= int(input('Escolha um Nivel de Dificuldade: '))

    if nivel == 1 :
        tentativa  = 3
        break 

    elif nivel == 2 :
        tentativa  = 2 
        break
    elif nivel == 3:
        tentativa  = 1 
        break
    else:
        print('Valor invalido')
        print('Tente Novamente')

print(f'VOCÊ TEM {tentativa} TENTATIVAS!')
############## CORPO DO JOGO ##########
Numero_secreto = randint(0,10)

for i in range(0, tentativa):

    Seu_numero = int(input('Digite um número de 0 a 10: '))
    Acertou = Numero_secreto == Seu_numero
    Errou = Numero_secreto != Seu_numero
    Menor = Numero_secreto > Seu_numero
    Maior = Numero_secreto < Seu_numero
    
    if Seu_numero < 0 or Seu_numero> 10:
        print('Numero Invalido!')
        continue
    if (Acertou):
        print('Parabéns Você acertou o número')
        print('VOCÊ VENCEU !!!!')  
        break
    if i == tentativa - 1:
            print('VOCÊ PERDEU !!!!') 
            break 
    elif (Errou):
        print('Você Errou o Número')
        if (Maior):
            print('Tente um valor mais Baixo.')
        elif(Menor):
            print('Tente um valor Maior.')    
        
                
print('FIM DE JOGO!')    