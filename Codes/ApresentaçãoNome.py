num_sobrenome = int(input('quantos sobrenomes seu nome possui ? '))
nc = str(input('Digite seu nome completo: '))
apelido = int(input('qual dos dois nomes vôce gosta de ser chamado (1 ou 2): '))

if apelido == 1:
    apelido = 0
if apelido == 2:
    apelido = 1

first_name = nc.split()[apelido]
sn = ' '.join(nc.split()[num_sobrenome:])

print('Óla {}, gostei do seu sobrenome {}'.format(first_name, sn))