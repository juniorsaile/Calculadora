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
      [7] Sair.''')
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
