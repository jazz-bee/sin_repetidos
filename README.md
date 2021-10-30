# Sin repetidos

Función que recibe dos parámetros: un string S y un integer R.

La función devuelve un string donde los caracteres consecutivos de S no se repitan más que R veces.
(un string con el texto limpio y la cantidad de caracteres repetidos correcta)

Ejemplos:

 Ej1: "AAAAAFFFFOOOA", 2 => "AAFFOOA"

 Ej2: "111223333344", 1 => "1234"
 
 Ej3: "AABB", 1 => "AB"


## Pseudocodigo
 1) recorrerlo hasta el final del string
 2) leer caracter
 3) guardar caracter
 3) contar caracter
 4) comparar caracter
 5) guardar caracter UTIL en otra variable

## Probar
Para probar la función se crearon tests utilizando ***pytest***.

Se recomienda crear un entorno virtual 

### Steps

``` python3 -m venv venv ``` 

```source venv/bin/activate```

```pip install pytest```

```pytest test_ejercicio.py``` 
