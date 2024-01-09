menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
global saldo
saldo: float = 0.0
limite = 500
extratoConta = []
global numeroSaques
numeroSaques = 0
LIMITE_SAQUES = 3

def depositar() -> float:
  global saldo
  valorDeposito = 0
  
  while valorDeposito <= 0:
    try:
      valorDeposito = round(float(input("Valor de depósito: R$ ")),2)
    except:
      print("É permitido apenas números, separe os centavos utilizando '.'")

  saldo += valorDeposito
  print(f'Seu saldo atual é de R$ {saldo:.2f}')
  extrato("Depósito", f'+ R$ {valorDeposito:.2f}', f'R$ {saldo:.2f}')
  return saldo

def sacar() -> float:
  global numeroSaques
  global saldo
  valorSaque = 0.0
  
  while valorSaque <= 0:
    try:
      valorSaque = round(float(input(f'Valor de saque: R$ ')),2)
    except:
      print("É permitido apenas números, separe os centavos utilizando '.'")
  
  if valorSaque > limite:
    print(f"Não é permitido realizar um saque maior que {limite:.2f}")
  
  elif valorSaque > saldo:
    print("Saldo insuficiente para valor de saque")
  
  elif numeroSaques >= LIMITE_SAQUES:
    print(f"Não é permitido realizar mais que {LIMITE_SAQUES} saques por dia")
  
  elif valorSaque > limite:
    print(f"Não é possível realizar um saque maior que {limite:.2f}")
  
  else:
    saldo -= valorSaque
    numeroSaques += 1
    print(f'Seu saldo atual é de R$ {saldo:.2f}')
    extrato("Saque", f'- R$ {valorSaque:.2f}', f'R$ {saldo:.2f}')
    return saldo

def extrato(transacao, valorTransacao, saldo):
  dataTransaction = {
    "Transação":transacao,
    "Valor":valorTransacao,
    "Saldo":saldo
  }

  extratoConta.append(dataTransaction)


if __name__ == "__main__":
  while True:

    opcao = input(menu)

    if opcao == "d":
      depositar()

    elif opcao == "s":
      sacar()
    
    elif opcao == "e":
      if len(extratoConta) == 0: 
        print("Não foram realizadas movimentações")
      else:
        for element in extratoConta:
          for elm in element.keys():
            if elm == 'Saldo':
              print()
              print(f"Saldo:            {element[elm]}")
            else:
              print(f"{element[elm]:15}", end=" ")
    
    elif opcao == "q":
      print("Saindo...")
      break
    
    else:
      print("Operação inválida, por favor selecione novamente a opção desejada.")
