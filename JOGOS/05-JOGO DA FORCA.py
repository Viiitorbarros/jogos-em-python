def jogar_forca():
    ############## NOME ##########
    print('-=-'*10)
    print('Bem vindo ao Game da Forca.')
    print('-=-'*10)
    ############## Variaveis ##########

    palavra_secreta = 'carro'.upper()
    tentativas = 6
    resultado =["_" for i in palavra_secreta ]
    
    ############## CORPO DO JOGO ##########
    while True: 
        print(resultado)
        if (tentativas != 0):    
            print (f'Voce tem {tentativas} tentativas sobrando:')
        elif (tentativas == 0): 
                print (f'Suas tentativas Acabaram.')
                print(' -> VOCE ENFORCOU!!!')
                break
        chute = str(input('Escolha uma letra:')).upper().strip()
        pos = 0
        if ( chute in palavra_secreta ):
            for letra in palavra_secreta:
                if (letra == chute):
                    print(f' -> Encontrei a letra {letra} na posição {pos+1} ')
                    resultado[pos] = letra
                pos +=1
        else:
            tentativas -= 1
        if ('_' not in resultado) :
            print ('--------------------------')   
            print(' -> Parabéns você venceu !!!')
            print(f' -> A Palavra era {resultado}')
            print ('--------------------------')  
            break

        print ('--------------------------')        
        
    print('Fim de jogo...!"')

if __name__ == "__main__":
    jogar_forca()    