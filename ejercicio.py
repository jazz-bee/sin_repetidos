# devuelve un string donde los caracteres consecutivos de S no se repitan más que R veces
def sin_repetidos(str,number):
    cantidad = 0
    final = ""
    anterior = ""
    for caracter in str:
        cantidad = cantidad+1
        if(caracter != anterior):
            cantidad=1
            anterior=caracter

        if(cantidad <= number):
            final = final + caracter 
    return final

