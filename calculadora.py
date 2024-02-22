from time import sleep

# sleep(2)
print('='*20)
print('Carregando...')
print('='*20)
# sleep(3)
print('''Segue abaixo as opções para utilizar:
      [1] Somar.
      [2] Subtrair.
      [3] Divisão.
      [4] Multiplicação.
      [5] Tabuada.
      [6] Menor e maior.
      [7] Progressão Aritmética.
      [8] Sequência de Fibonacci.
      [9] -
      [0] Sair.''')
opc = int(input('''Digite a opção na qual você deseja: '''))
while True:
    if opc == 1:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
#        sleep(1)
        print('Calculando...')
#        sleep(2)
        res = n1+n2
        print('{:.2f} + {:.2f} = {:.2f}'.format(n1, n2, res))
    elif opc == 2:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
#        sleep(1)
        print('Calculando...')
#        sleep(2)
        res = n1-n2
        print('{:.2f} - {:.2f} = {:.2f}'.format(n1, n2, res))
    elif opc == 3:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
#        sleep(1)
        print('Calculando...')
#        sleep(2)
        res = n1/n2
        print('{:.2f} : {:.2f} = {:.2f}'.format(n1, n2, res))
    elif opc == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
#        sleep(1)
        print('Calculando...')
#        sleep(2)
        res = n1*n2
        print('{:.2f} x {:.2f} = {:.2f}'.format(n1, n2, res))
    elif opc == 5:
        c = 0
        cont = 'a'
        n = int(input('Tabuada de qual número deseja saber? '))
        while c != 11:
            r = n * c
            print('{} x {} = {}'.format(n, c, r))
            c += 1
            if c == 11:
                while cont not in 'SsNn':
                    cont = input('Deseja continuar [S/N]: ').upper()
            if cont in 'Nn':
                break
        if cont in 'Nn':
            break
    elif opc == 6:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
        if n1 < n2:
            print(f'O número {n1} é o menor, e o número {n2} é o maior.')
        elif n2 < n1:
            print(f'O número {n2} é o menor, e o número {n1} é o maior.')
        else:
            print(f'Ambos os números {n1} e {n2} são iguais.')
    elif opc == 7:
        x = 0
        n1 = int(input('Digite o primeiro termo: '))
        n2 = int(input('Digite a razão termo: '))
        while True:
            print(f'{n1} → ', end='')
            n1 += n2
            x += 1
            if x == 11:
                break
        if x == 11:
            print('FIM')
            break
