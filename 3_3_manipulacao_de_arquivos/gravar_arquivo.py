with open("teste.txt","w") as arquivo:
  arquivo.write("Nunca foi tão fácil criar uma arquivo.")

# Ascrentar uma nova mensagem com "a" (append)
with open("teste.txt", "a") as arquivo:
  arquivo.write(" Continuação do texto.")