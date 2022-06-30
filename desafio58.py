from random  import randint
num = randint(1,10)

print("Sou seu computador e...\nAcabei de pensar em um número entre 0 e 10")
print('Será que você consegue advinhar?')
palpite = int(input('Qual o seu palpite? '))
cont = 1
while palpite != num:
    if palpite < num:
        print('Mais alto!')
    else:
        print('Mais baixo!')

    palpite = int(input("Você errou! Tente novamente: "))
    cont += 1


if cont == 1:
    print(f'Cagada da mulesta. Você acertou...\nMas antes de comemorar, se LIMPE!!!!')

elif cont == 10:
    print("Esse homi ta sem sorte vum!!!")

else:
    print(f'Acertou!!! Após {cont} tentativas.')

