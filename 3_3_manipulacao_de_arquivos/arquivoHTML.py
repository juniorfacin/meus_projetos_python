with open("pagina.html", "w") as pagina:
    pagina.write("<body> <h1> Este é um teste para página WEB </h1>")
    pagina.write("<h2>Abaixo segue alguns nomes importantes para o Projeto: </h2>")
    pagina.write("<h3>")
    nome = ""
    while nome != "SAIR":
        nome = input("Digite um nome para o Projeto ou SAIR: ").upper()
        if nome != "SAIR":
            pagina.write("<br>" + nome)
    pagina.write("</h3> </body>")
