#---------------------------------------------------------------------------------------

#COLECOES - COLLECTIONS
fracao = 4.50
# Lista (list) - tambem chamado de array
lista = [42, fracao, "Spam"]
print(lista)
print(lista[0])

print

#Tuplas (tuple) - faz o mesmo que lista, só que imutavel
tupla = (42, fracao, "Spam")

#Dicionarios - tipo listas, mas com chaves (keys)
dicionario = {"a":"Abelha", "b":"bulldog","c":"canario"}
dicionario2 = {1:"Abelha", 3: 2019, 2:"canario"}

print(dicionario) #mostra a variavel
print(dicionario["a"]) #mostra a variavel
print(*dicionario2) #mostra conteudo da variavel
print(dicionario2[2])
print(dicionario2[3])

for item in dicionario:
    print(dicionario[item])

