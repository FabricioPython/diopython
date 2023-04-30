
nome_cliente = input("Digite seu nome para começar: ")
print(f"\nBem vindo {nome_cliente}!,\nVoce já pode movimentar sua conta.")
print(70 * "-")

menu = """           

Selecione uma opção:

          1 - Depósito ----> [1]
          2 - Saque    ----> [2]
          
          3 - Extrato  ----> [3]
          4 - Sair     ----> [4]
          """
    
print(menu)
print(70 * "-")

saldo = 0.0
extrato = f"Saldo Atual: R$:{saldo:.2f} | Você não possui outros lançamentos \n"


while True:
    escolha = int(input("Selecione uma opção: "))
    print(70 * "-")


    if escolha == 1:

        valor = float(input("Digite o valor do depósito | R$:"))

        if valor > 0:
            saldo += valor
            valor
            print(saldo)
            extrato+= f"(+) Depósito, R$:{valor:.2f}\n(=) Saldo atual R$:{saldo:.2f} \n"
            print(70 * "-")

            
            
        else:
            print("Digite um valor maior que zero!")
            print(70 * "-")

            
    if escolha == 3:
        print(extrato)
        print(70 * "-")

        
        
    if escolha == 2:
        
        saque_valor = float((input("Digite um valor para saque | R$:")))
        
        if saque_valor < saldo:
            saldo = saldo - saque_valor
            print(f"Voce sacou R${saque_valor:.2f}")
            extrato+= f"(-) Saque: R${saque_valor:.2f}\n(=) Saldo atual: R${saldo:.2f}\n"
            print(70 * "-")

            
        else:
            print(f"Voce não possui limite disponivel para esse saque, saldo atual: R${saldo:.2f}")
            print(70 * ">")

            
        
    if escolha == 4:
        break



