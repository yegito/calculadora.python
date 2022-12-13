def calcular():                                                        ##Função para capturar o operador 
    operador = input('''
Por favor, digite a operação matemático que você quer usar:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

    number_1 = int(input('Por favor entre com o primeiro numero: '))
    number_2 = int(input('Por favor entre com o segundo numero: '))

    if operador == '+':                                                    ##Condições para identificar os operadores 
        print(f'{number_1} + {number_2} = ')               
        print(number_1 + number_2)

    elif operador == '-':
        print(f'{number_1} - {number_2} = ')
        print(number_1 - number_2)

    elif operador == '*':
        print(f'{number_1} * {number_2} = ')
        print(number_1 * number_2)

    elif operador == '/':
        print(f'{number_1} / {number_2} = ')
        print(number_1 / number_2)

    else:
        print('Esse operador não é valido.')
        novamente()


def novamente():                                                           ##Uma função para restartar a calculadora 
    calcular_denovo = input('''
Você quer calcular novamente??
Por favor escreva Y para SIM ou N para NÃO.
''')

    if calcular_denovo.upper() == 'Y':
        calcular()
    elif calcular_denovo.upper() == 'N':
        print('Até mais.')
    else:
        novamente()


calcular()