from turtle import Turtle


'''
shape(<formato>) — indica o formato que a tartaruga deve ter.
color(<cor>) — indica a cor que a tartaruga pode ter.
forward(<distancia>) ou fd(<distância>)— indica quantos pixels de distância a tartaruga deve andar para frente.
back(<distância>) ou bk(<distancia>) — indica quantos pixels de distância a tartaruga deve andar para trás.
right(<ângulo>) — indica a rotação, em graus de ângulo, à direita que a tartaruga deve fazer.
left(<ângulo> — indica a rotação, em graus de ângulo, à esquerda que a tartaruga deve fazer.
home() — movimenta a tartaruga para a origem do sistema de coordenadas (centro do canvas).
speed(<velocidade>) — indica a velocidade da caneta, sendo um valor entre 1 e 10:
clear() — limpa todo o canvas, removendo tudo que foi desenhado
tartaruga.forward(100)
tartaruga.right(90)
tartaruga.back(100)
tartaruga.left(90)
tartaruga.forward(100)
'''


def frente_tras(ft):
    if ft in 'f':
        pf = int(input('Quantos px você quer que ela ande?: '))
        tartaruga.forward(pf)

    else:
        pt = int(input('Quantos px você quer que ela ande?: '))
        tartaruga.back(pt)


def direita_esquerda(d_e):
    if d_e in 'd':
        graus = int(input('Quantos graus você quer que ela vire?: '))
        tartaruga.right(graus)

    else:
        graus = int(input('Quantos graus você quer que ela vire?: '))
        tartaruga.left(graus)


def continuar(resp):
    global jogar
    jogar = False
    if resp in 's':
        print('Vamos iniciar novamente..............')
        jogar = True
    else:
        jogar == False


tartaruga = Turtle()
tartaruga.shape("turtle")
tartaruga.color('dark green')
tartaruga.speed(1)
espacos = '#' * 10


print('#' * 50)
print(f'{espacos} Bem vindo ao mini-game turtle. {espacos}')
nome = input('Digite seu nome: ')
email = input('Digite seu e-mail: ')
print('#' * 50)
print(f'{espacos} Ok {nome} vamos jogar um pouco! {espacos}')
print(f'{espacos} Você vai movimentar a tartaruga! {espacos}')

jogar = True
while jogar == True:
    d_e = input(
        'Você quer ir com a tartaruga para direira ou para esquerda? (Responda "d" para direita e "e" para esquerda)')
    direita_esquerda(d_e)
    
    ft = input('Você quer ir com a tartaruga para frente ou para trás? ' +
               '(Responda "f" para frente e "t" para trás)')
    frente_tras(ft)

    jogar = str(
        input('Quer continuar a desenhar/brincar? Digite "s" para Sim e "n" para não.'))
    continuar(jogar)
    

print('Muito Obrigado por jogar comigo!')
