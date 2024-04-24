nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if (idade >= 65):
  print(f"O paciente {nome}, tem {idade} anos de idade e POSSUI atendimento prioritário")
else:
  print(f"O paciente {nome}, tem {idade} anos de idade e NÃO POSSUI atendimento prioritário")