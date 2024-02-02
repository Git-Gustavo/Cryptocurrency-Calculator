'''
Quantidade investidade 
Preço de compra 
Venda   cripto atual x quantidade de cripto
---------------
compra/ cripto*(1-0,9%/100)*(1+0,9%/100)
'''


while True:
    try:
        compra = float(input('Quantidade investidade: '))
        cripto = float(input('Preço da compra de cada Criptomoeda: '))
        tabela = print("\n1 ---> Lucro líquido \n2 ---> Preço da moeda ^\n3 ---> Sair")
        iniciar = int(input('Digite um numero correspondente ao que esta acima: '))

        if iniciar == 1:
            venda = float(input('Preço da venda da Criptomoeda: '))
            quantidade = compra / cripto
            lucro_bruto = quantidade * venda - compra
            imposto = 0.0018 * lucro_bruto
            lucro_liquido = lucro_bruto - imposto
            print("O lucro foi de {:.2f}".format(lucro_liquido))
            print('---------------------------------------------------------------------')
        elif iniciar == 2:
            equilibrio = cripto + (cripto* (1.8/100))
            print(equilibrio)
            print('---------------------------------------------------------------------')
        elif iniciar == 3:
            break

        else:
            print('Invalido')

        



    
    except ValueError:
        print("Por favor, insira um valor numérico válido.")
        print('---------------------------------------------------------------------')

 