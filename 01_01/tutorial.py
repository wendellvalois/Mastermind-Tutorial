
# VARIAVEIS EM PYTHON

#inteiro (integer)
numerica = 6
#ponto flutuante (float)
fracao = 4.50
#string : conjunto de caracteres 
string_exemplo = "Azul"

print(string_exemplo)
print(string_exemplo[1])
print("primeira letra: ", string_exemplo[0])

# Nota: especificamente em python string_exemplos sao imutaveis
# string_exemplo[0] = "p"   
# print(string_exemplo)

variavel_auxiliar = list(string_exemplo)
variavel_auxiliar[0] = "X"
string_exemplo = "".join(variavel_auxiliar)
print(string_exemplo)

#no entanto pode refazer, no caso destroi o conteudo e refaz o que tem dentro
string_exemplo = "A mesma string_exemplo com outras coisas"
print(string_exemplo)

