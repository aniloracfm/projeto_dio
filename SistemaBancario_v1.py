QUANT_SAQUE_MAX = 3
SAQUE_MAX       = 500
saldo_total     = 0

def func_dep():
    global saldo_total
    msg_dep = '### depósito ###'
    msg_dep = msg_dep.title()

    print(msg_dep)
    print(f'Digite o valor para depósito: ')

    valor_deposito = float(input())
    saldo_total    = saldo_total + valor_deposito

    print(saldo_total)

    msg_dep_feito = (f'Depósito de R${valor_deposito} feito com sucesso.')

    print()
    print(msg_dep_feito)

    return saldo_total



def func_saque():
    global saldo_total
    global QUANT_SAQUE_MAX
    msg_saq = '### Saque ###'
    msg_saq = msg_saq.title()

    print(msg_saq)
    print(f'Digite o valor para saque: ')
    valor_saque = float(input())

    if saldo_total >= valor_saque:

      if valor_saque <= SAQUE_MAX:
        if QUANT_SAQUE_MAX >= 3:
          saldo_total = saldo_total - valor_saque
          print(f'Saque de {valor_saque} feito com sucesso.')
          QUANT_SAQUE_MAX -= 1
        else: 
          print()
          print(f'Limite diário de saque atingido.')
      else:
        print()
        print(f'Não é possível realizar saque acima de R$500,00.')

    else:
      print(f'Não foi possível concluir o saque de valor {valor_saque}.')

    return saldo_total

def func_extra():   
  msg_ext = (f'''### Extrato ###
 Saldo em Conta: {saldo_total}''')

  print(msg_ext)


def func_menu():
  print("_____________________________________")
  print(f'''     ### MENU ### 
 Escolha uma operação:
 1- Depósito
 2- Saque
 3- Extrato
 4- Sair ''')

  opcao = int(input(f'-> '))
  return opcao


while True:
  opcao = func_menu()
  print()
  if opcao == 1:
    func_dep()
  elif opcao == 2:
    func_saque()
  elif opcao == 3:
    func_extra()
  else:
    print("Encerrando programa...")
    break



