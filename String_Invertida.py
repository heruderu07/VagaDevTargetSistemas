def inverter_string(s):
    string_invertida = ""
    
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    
    return string_invertida

entrada = input("Informe uma palavra ou frase para inverter a ordem das letras: ")

resultado = inverter_string(entrada)

print(f"A palavra ou frase invertida ficou assim: {resultado}")
