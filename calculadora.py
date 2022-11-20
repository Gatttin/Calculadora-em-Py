#Calculadora em py
########################

#criar menu
#perguntar pro usuário qual tipo de calculo
#calculo dos 2 numeros
#imprimir resultado na tela no menu
#aviso se a msg estiver errada

print('='*50)

msg = 'Calculadora 2.0'
print('{:.^50}'.format(msg))
print('='*50)

def adicao():
    a = float(input("primeiro valor: "))
    b = float(input("segundo valor: "))
    resultado = a + b
    print(f'Total:{resultado}')
    
def subtrair():
    a = float(input("primeiro valor: "))
    b = float(input("segundo valor: "))
    resultado = a - b
    print(f'Total:{resultado}')
    
def multiplicacao():
    a = float(input("primeiro valor: "))
    b = float(input("segundo valor: "))
    resultado = a * b
    print(f'Total:{resultado}')

def divisao():
    a = float(input("primeiro valor: "))
    b = float(input("segundo valor: "))
    resultado = a / b
    print(f'Total:{resultado}')
    
opcao = 0

while opcao != 4:
    print('Menu:\n1.adicao\n2.subtrair\n3.multiplicacao\n4.divisao\n5.Sair da calculadora')
    opcao = int(input('>'))
    if opcao == 1:
        adicao()
    elif opcao == 2:
        subtrair()
    elif opcao == 3:
        multiplicacao()
    elif opcao == 4:
        divisao()
    elif opcao == 5:
        print('Saindo do programa')
        break
    else: 
        print('Opção Invalida, tente novamente.')