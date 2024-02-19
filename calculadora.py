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
      [5] Menor e maior.
      [6] Tabuada.
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
        n1 = float(input('Digite um número'))
