import textwrap
menu = """\n
================= MENU =================
[CU]\tCadastrar usuário
[NC]\tNova conta
[D]\tDepositar
[S]\tSacar
[E]\tExtrato
[LC]\tListar contas
[Q]\tSair

=> """

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

def criarUsuario(usuarios):
  # usuarioExiste = False
  
  usuario = {
    "nome": None,
    "sobrenome": None,
    "dataNascimento":None,
    "CPF":None,
    "endereco":{
      "logradouro": None,
      "numero": None,
      "bairro": None,
      "cidade": None,
      "siglaEstado": None
    },
  }
  cpf = input("Por favor, digite seu CPF:")
  usuarioExistente = filtrarUsuario(cpf, usuarios)

  if usuarioExistente:
    print("Usuário já cadastrado!")
    return
  
  usuario["CPF"] = cpf
  usuario["nome"] = input("Primeiro nome: ").upper()
  usuario["sobrenome"] = input("Sobrenome: ").upper()
  usuario["dataNascimento"] = input("Data de nascimento (DD/MM/AAAA): ")
  usuario["endereco"]["logradouro"] = input("Logradouro: ").upper()
  usuario["endereco"]["numero"] = input("Número da residencia: ")
  usuario["endereco"]["bairro"] = input("Bairro: ").upper()
  usuario["endereco"]["cidade"] = input("Cidade: ").upper()
  usuario["endereco"]["siglaEstado"] = input("Estado (UF): ").upper()
  usuarios.append(usuario)

def filtrarUsuario(cpf, usuarios):
  usuariosFiltrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
  return usuariosFiltrados[0] if usuariosFiltrados else None

def criarContaCorrente(AGENCIA, numeroConta, usuarios):
  cpf = input("Digite aqui seu CPF (somente os números):")
  usuario = filtrarUsuario(cpf, usuarios)

  if usuario:
    conta = {
      "agencia": AGENCIA,
      "numeroConta": numeroConta,
      "usuario": usuario
    }
    print("### Conta criada com sucesso! ###")
    return conta
  print("### Cliente não cadastrado, você será redirecionado(a) ao menu! ###")

def listarContas(contas):
  for conta in contas:
    linha = f"""\
      Agência:\t{conta['agencia']}
      C/C:\t\t{conta['numeroConta']}
      Titular:\t{conta['usuario']['nome'] + " " + conta['usuario']['sobrenome'] }
    """
    print("=" * 100)
    print(textwrap.dedent(linha))
  
if __name__ == "__main__":
  
  LIMITE_SAQUES = 3
  AGENCIA = '0001'

  saldo: float = 0.0
  limite = 500
  numeroSaques = 0
  extratoConta = []
  usuarios = []
  contas = []

  while True:
    opcao = input(textwrap.dedent(menu)).upper()

    if opcao == "CU":
      criarUsuario(usuarios)

    elif opcao == "NC":
      numeroConta = len(contas) + 1
      conta = criarContaCorrente(AGENCIA, numeroConta, usuarios)

      if conta:
        contas.append(conta)

    elif opcao == "D":
      depositar()

    elif opcao == "S":
      sacar()
    
    elif opcao == "E":
      if len(extratoConta) == 0: 
        print("Não foram realizadas movimentações")
      else:
        for extrato in extratoConta:
          linha = f"""\
            Valor:\t{extrato['Valor']}
            Saldo:\t  {extrato['Saldo']}
          """
          print("=" * 100)
          print(textwrap.dedent(linha))
    
    elif opcao == "Q":
      print("Saindo...")
      break
    
    elif opcao == "LC":
      listarContas(contas)  

    else:
      print("Operação inválida, por favor selecione novamente a opção desejada.")
