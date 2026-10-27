def maior_iterativo(lista):
    if not lista:
        raise ValueError("A lista não pode estar vazia.")

    maior = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero

    return maior

def maior_recursivo(lista):
    if not lista:
        raise ValueError("A lista não pode estar vazia.")

    if len(lista) == 1:
        return lista[0]

    maior_restante = maior_recursivo(lista[1:])

    if lista[0] > maior_restante:
        return lista[0]

    return maior_restante

def valida_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")

    if not cpf.isdigit() or len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    numeros = [int(digito) for digito in cpf]

    # Calcula o primeiro dígito verificador
    soma = sum(numeros[i] * (10 - i) for i in range(9))
    resto = soma % 11

    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    if numeros[9] != digito1:
        return False

    # Calcula o segundo dígito verificador
    soma = sum(numeros[i] * (11 - i) for i in range(10))
    resto = soma % 11

    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    if numeros[10] != digito2:
        return False

    return True

if __name__ == "__main__":
    numeros = [3, 9, 2, 7]

    print("Lista:", numeros)
    print("Maior iterativo:", maior_iterativo(numeros))
    print("Maior recursivo:", maior_recursivo(numeros))

    print("CPF válido:", valida_cpf("529.982.247-25"))
    print("CPF inválido:", valida_cpf("111.111.111-11"))

    