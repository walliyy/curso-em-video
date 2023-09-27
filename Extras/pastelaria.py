def menu(total_pedido=0):
    while True:
        print(
            'Bem-Vindo a Pastelaria Novo Paladar \n'
            'Opções disponíveis: \n'
            '1 - PASTEIS \n'
            '2 - BEBIDAS \n'
            '3 - SOBREMESAS \n'
            '0 - FINALIZAR PEDIDO \n'
            'Total do Pedido: R$ {:.2f} \n'.format(total_pedido)           
        )

        op = int(input('Escolha a Opção desejada: '))

        match op:
            case 1:
                total_pedido += pasteis()
            case 2:
                total_pedido += bebidas()
            case 3:
                total_pedido += sobremesas()
            case 0:
                finalizar(total_pedido)
                break
            case _:
                print('Opção Inválida, favor selecionar novamente \n')

def pasteis():

    # # variable declaration
    vpc = 12.50
    vpf = 12.50
    vpq = 14.50
    tpc = 0.00
    tpf = 0.00
    tpq = 0.00

    while True:
        print(
            'Pasteis diponíveis: \n'
            '1 - Pastel de Carne --- R$ 12,50 \n'
            '2 - Pastel de Frango -- R$ 12,50 \n'
            '3 - Pastel de queijo -- R$ 14,50 \n'
            '0 - Menu Anterior \n'           
        )

        op = int(input('Escolha a opção desejada: '))
    
        # while op != 0:
        #     pasteis()
        match op:
            case 1:
                qntd = int(input('Informe a quantidade desejada: '))
                pc = qntd * vpc
                tpc = pc
                # pasteis()
            case 2:
                qntd = int(input('Informe a quantidade desejada: '))
                pf = qntd * vpf
                tpf = pf
                # pasteis()
            case 3:
                qntd = int(input('Informe a quantidade desejada: '))
                pq = qntd * vpq
                tpq = pq
                # pasteis()
            case 0:
                tp = tpc + tpf + tpq
                return tp
            case _:
                print('Opção Inválida, favor selecionar novamente \n')
                # pasteis()

def bebidas():
    print('Bebidas')

def sobremesas():
    print('Sobremesas')

def finalizar(total_pedido):
    print('\nTotal do Pedido: R$ {:.2f}'.format(total_pedido))
    print('Pedido finalizado. Obrigado!')

menu()