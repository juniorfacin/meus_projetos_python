# Dicionário vazio
usuarios = {}

# Dicionário com 02 objetos com chaves de nome "Chaves" e "Quico"
usuarios = {
    "Chaves":["Chaves Silva","17/06/2017","Recep_01"],
    "Quico":["Enrico Flores","03/06/2017","Raiox_02"]
    }

# Adicionar um novo objeto, com chave "Florinda"
# Se dividir em 2 momentos a última linha irá sobrepor os objetos inseridos anteriormente naquela chave.
# usuarios["Florinda"] = ["Florinda Flores"]
# usuarios["Florinda"] = ["26/11/2017", "Recep_01"]

# Forma correta para adicionar
usuarios["Florinda"] = ["Florinda Flores", "26/11/2017", "Recep_01"]

# Se adicionarmos um objeto com a mesma chave, o último irá sobrescrever os anterioresusuarios={}
usuarios = {
    "Chaves":["Chaves Silva","17/06/1975","Recep_01"],
    "Quico":["Enrico Flores","03/06/1976","Raiox_02"],
    "Quico":["Enrico Flores","03/06/1976","Raiox_03"]
    }
usuarios["Florinda"] = ["Florinda Flores", "26/11/2017", "Recep_01"]
usuarios["Florinda"] = ["Florinda Flores", "26/11/2016", "Recep_01"]

print(usuarios)
print("######=======######")
print(f"Dados: {usuarios.get("Chaves")}")
print("Dados: ", usuarios.get("Chapolim"))