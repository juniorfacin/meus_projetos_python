nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
prioridade = "NÃO"
if (idade >= 65):
  prioridade = "SIM"

print(f"O paciente {nome} possui atendimento prioritário? {prioridade}.")