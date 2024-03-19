#contenuto = ("id,nome,cognome,eta\n")

file_uno = open("dati.txt", "a")

id = input("Inserisci un Id: \n")
nome = input("Inserisci il Nome: \n")
cognome = input("Inserisci il Cognome: \n")
eta = input("Inserisci l'Età: \n")

file_uno.write(id+","+nome+","+cognome+","+eta)
file_uno.close()
file_uno = open("dati.txt", "r")

print("Il numero di righe è: " + str(len(file_uno.readlines())))
file_uno.close()

file_uno = ("dati.txt ")
id_linea = input("Inserisci l'id da cercare: \n")
file = open(file_uno, "r")

for linea in file:
    if linea.startswith(id_linea):
        print("Risultato trovato:", linea)
        break
else:
    print("Nessun risultato: o per l'id: ", id_linea)

test = ("2,dd,ff,21")
div = test.split(",", 2)
print(div)
nuovo_nome = input("Inseerisci il nuovo nome: ")
Risultato = div[0] + "," + nuovo_nome + "," + div[2]
print(Risultato)

