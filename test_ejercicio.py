import pytest
import ejercicio


def test_sin_repetidos():

    # Si el string esta vacio, devolvera un string vacio
    assert ejercicio.sin_repetidos("",2)==""

    # Si r=0, para todo string de entrada, la salida sera un string vacio
    assert ejercicio.sin_repetidos("AABB",0)==""

    # Los caracteres consecutivos de S no se repitan más que R veces
    assert ejercicio.sin_repetidos("AAAAAFFFFOOOA",2)=="AAFFOOA"
    assert ejercicio.sin_repetidos("111223333344",1)=="1234"
    assert ejercicio.sin_repetidos("AABB",1)=="AB"

    # Se admiten todo tipo de caracteres
    assert ejercicio.sin_repetidos("AA12BBBB33#'",2)=="AA12BB33#'"

    # Letras minusculas y mayusculas son distintos caracteres y no cuenta como repetido
    assert ejercicio.sin_repetidos("aaaAaBbc",1)=="aAaBbc"

    #Si R es un entero negativo devuelve una cadena vacia
    assert ejercicio.sin_repetidos("AABB",-1)==""

