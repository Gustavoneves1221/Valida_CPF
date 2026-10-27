import random 
import utilidades

digitos = []

for i in range(10):
    digitos.append(random.randint(1,100))

print("Numeros gerados: ", digitos)

maior = utilidades.maior_iterativo(digitos)
print("Maior nuemro iterativo: ", maior)

maior_rec = utilidades.maior_iterativo(digitos)
print("Maior numero recursivo: ", maior_rec)