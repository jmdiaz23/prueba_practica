"""
Se le da una cadena S. S contiene solo caracteres alfanumericos. Su tarea es ordenar la cadena S
de la siguiente manera:
Todas las letras minusculas ordenadas estan por delante de las mayusculas.
Todas las letras mayusculas ordenadas estan por delante de los dıgitos.
Todos los dıgitos impares ordenados estan por delante de los dıgitos pares ordenados
"""

def ordenar_cadena(S):
    if not 0 < len(S) < 1000:
        return "Error: la longitud de la cadena debe ser mayor que 0 y menor que 1000"

    letras_minusculas = []
    letras_mayusculas = []
    digitos_impares = []
    digitos_pares = []
    
    for caracter in S:
        if caracter.islower():
            if caracter not in letras_minusculas:
                letras_minusculas.append(caracter)
        elif caracter.isupper():
            if caracter not in letras_mayusculas:
                letras_mayusculas.append(caracter)
        elif caracter.isdigit():
            if int(caracter) % 2 == 0:
                if caracter not in digitos_pares:
                    digitos_pares.append(caracter)
            else:
                if caracter not in digitos_impares:
                    digitos_impares.append(caracter)
    
    letras_minusculas.sort()
    letras_mayusculas.sort()
    digitos_impares.sort()
    digitos_pares.sort()
    
    return ''.join(letras_minusculas + letras_mayusculas + digitos_impares + digitos_pares)


cadena = "Sorting1234"
cadena_ordenada = ordenar_cadena(cadena)
print(cadena_ordenada) # ginortS1324
