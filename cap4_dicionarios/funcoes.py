def perguntar():
  resposta = input("O que deseja realizar?\n <I> - Para inserir um usuário \n<P> - Para pesquisar um usuário \n<E> - Para excluir um usuário \n<L> - Para Listar um usuário: ").upper()
  return resposta

def inserir(dicionario):
    dicionario [input("Digite o login: ").upper()] =[input("Digite o nome: ").upper(), input("Digite a última data de acesso: "),input("Qual a última estação acessada: ").upper()]

def pesquisar(dicionario, chave):
  lista = dicionario.get(chave)
  if lista != None:
    print(f"Nome............: {lista[0]}")
    print(f"Último acesso...: {lista[1]}")
    print(f"Última estação..: {lista[2]}")

def excluir(dicionario, chave):
  if dicionario.get(chave) != None:
    del dicionario[chave]
  print("Objeto eliminado.")

def listar(dicionario):
  for chave, valor in dicionario.items():
    print("Objeto......")
    print(f"Login: {chave}")
    print(f"Dados: {valor}")
    
  