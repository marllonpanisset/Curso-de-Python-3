# Desenvolva um programa que leia as duas notas
# De um aluno, calcule e mostre a sua média.
av1 = float(input('Digite sua nota para AV1: '))
av2 = float(input('Digite sua nota para AV2: '))
media = av1 + av2
if media >= 7:
    print('Parabéns, você foi aprovado!')
else:
    print('Sinto muito, mas você ficou de recuperação. Sua média foi {}, você precisa de uma nota maior ou igual a 7.'.format(media))
    av3 = float(input('Qual sua nota para recuperação: '))
    if av3 >= 7:
        print('Parabéns, você foi aprovado e sua média é {}!'.format(av3))
    else:
        print('Sinto muito, você foi reprovado!')