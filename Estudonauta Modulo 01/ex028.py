from random import randint
sorteio = randint(1,10)
palpite = int(input('Em que número estou pensando? '))
if palpite == sorteio:
    print('PARABÉNS! Você adivinhou no número em que eu estava pensando, no caso {}.'.format(sorteio))
else:
    print('Não foi desta vez! Eu estava pensando no número {}, e você chutou o número {}.'.format(sorteio, palpite))
