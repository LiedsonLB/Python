import time

converter = str(input('Deseja converter de anos para meses ou meses para anos?(sim/não) '))

time.sleep(1)
if converter == 'sim'.lower():
    converter_why = str(input('Deseja converter anos ou meses ?'))
    if converter_why == 'anos':
        num_anos = int(input('quantos anos: '))
        meses = num_anos * 12
        print('O total de meses é {}'.format(meses))

    if converter_why == 'meses':
        num_anos = int(input('quantos meses: '))
        anos = num_anos / 12
        print('O total de meses é {}'.format(anos))

if converter == 'nao':
    print('Ok então, prossiga')

time.sleep(1)

escolha = str(input('O que deseja saber(juros, capital, taxa, periodo): '))


if escolha == 'juros':
    c = float(input('Digite o  valor: '))
    i = float(input('Digite a taxa ao mês sem o %: '))
    t = float(input('Digite o periodo em meses: '))

    j = (c * i * t) / 100

    print('=' * 42)
    print('Você teve um juros de {} reais '.format(j))
    print('Total a ser pago, {} reais'.format(c + j))
    print('=' * 42)
if escolha == 'capital':
    j = float(input('Digite o  juros: '))
    i = float(input('Digite a taxa ao mês sem o %: '))
    t = float(input('Digite o periodo em meses: '))

    c = (j * 100) / (i * t)

    print('=' * 42)
    print('Você teve um capital de {} reais '.format(c))
    print('Total a ser pago, {} reais'.format(c + j))
    print('=' * 42)
if escolha == 'taxa':
    c = float(input('Digite o  valor: '))
    j = float(input('Digite a juros: '))
    t = float(input('Digite o periodo em meses: '))

    i = (j * 100) / (c * t)

    print('=' * 42)
    print('Você teve uma taxa de {} % ao mês'.format(i))
    print('Total a ser pago, {} reais'.format(c + j))
    print('=' * 42)
if escolha == 'periodo':
    c = float(input('Digite o  valor: '))
    j = float(input('Digite o juros: '))
    i = float(input('Digite a taxa ao mês sem o %: '))

    t = (j * 100) / (c * i)

    print('=' * 42)
    print('Você teve um periodo de {} meses '.format(t))
    print('Total a ser pago, {} reais'.format(c + j))
    print('=' * 42)

continued = str(input('Deseja fazer algum calculo ? '))

while continued == 'sim'.lower():
    converter = str(input('Deseja converter de anos para meses ou meses para anos? '))

    time.sleep(1)
    if converter == 'sim':
        converter_why = str(input('Deseja converter anos ou meses ?'))
        if converter_why == 'anos':
            num_anos = int(input('quantos anos: '))
            meses = num_anos * 12
            print('O total de meses é {}'.format(meses))

        if converter_why == 'meses':
            num_anos = int(input('quantos meses: '))
            anos = num_anos / 12
            print('O total de meses é {}'.format(anos))

    if converter == 'nao':
        print('Ok então, prossiga')

    time.sleep(1)

    escolha = str(input('O que deseja saber(juros, capital, taxa, periodo): '))

    if escolha == 'juros':
        c = float(input('Digite o  valor: '))
        i = float(input('Digite a taxa ao mês sem o %: '))
        t = float(input('Digite o periodo em meses: '))

        j = (c * i * t) / 100

        print('=' * 42)
        print('Você teve um juros de {} reais '.format(j))
        print('Total a ser pago, {} reais'.format(c + j))
        print('=' * 42)
    if escolha == 'capital':
        j = float(input('Digite o  juros: '))
        i = float(input('Digite a taxa ao mês sem o %: '))
        t = float(input('Digite o periodo em meses: '))

        c = (j * 100) / (i * t)

        print('=' * 42)
        print('Você teve um capital de {} reais '.format(c))
        print('Total a ser pago, {} reais'.format(c + j))
        print('=' * 42)
    if escolha == 'taxa':
        c = float(input('Digite o  valor: '))
        j = float(input('Digite a juros: '))
        t = float(input('Digite o periodo em meses: '))

        i = (j * 100) / (c * t)

        print('=' * 42)
        print('Você teve uma taxa de {} % ao mês'.format(i))
        print('Total a ser pago, {} reais'.format(c + j))
        print('=' * 42)
    if escolha == 'periodo':
        c = float(input('Digite o  valor: '))
        j = float(input('Digite o juros: '))
        i = float(input('Digite a taxa ao mês sem o %: '))

        t = (j * 100) / (c * i)

        print('=' * 42)
        print('Você teve um periodo de {} meses '.format(t))
        print('Total a ser pago, {} reais'.format(c + j))
        print('=' * 42)

    continued = str(input('Deseja fazer algum calculo ? '))
    if continued == 'nao'.lower():
        break
