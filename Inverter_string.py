def inverter_string(s):
    tamanho = len(s)
    string_invertida = ""

    for i in range(tamanho - 1, -1, -1):
        string_invertida += s[i]

    return string_invertida

entrada_usuario = input("DIgite uma string: ")
resultado = inverter_string(entrada_usuario)

print("String original: ", entrada_usuario)
print("String invertida: ", resultado)