# se define la función de las operaciones básicas con 3 parámetros
# OPS es la operación, Op1 es el operando 1 y Op2 es el operando 2
# se usan condicionales para la elección de cada operación distinta.


def basic_operations(OPS, Op1, Op2):
    try:  # se utiliza la función try-except para validar las operaciones
        if int(OPS) == 1:  # con la operación igual a 1, es una suma
            return Op1+Op2  # se retorna la operación suma
        elif int(OPS) == 2:  # con la operación igual a 2, es una resta
            return Op1-Op2  # se retorna la operación resta
        elif int(OPS) == 3:  # con la operación igual a 3, es una división
            return Op1/Op2  # se retorna la operación división
        else:  # se ejecuta en cualquier otro caso
            return ("Error 4")  # corresponde a operación no soportada
    except ZeroDivisionError:  # excepción con el error de división por 0
        return ("Error 2")  # se retorna el Error 2 de división por 0
    except ValueError:  # excepción con el error de digitar valor erróneo
        return ("Error 1")  # se retorna el Error 1
# "Error 1" es equivalente a digitar un caracter diferente a un número


def count_char(sentence):  # se define otra función con un único parámetro
    count = 0  # se define la varible count con un valor de cero
    if sentence.isnumeric():  # este comando verifica si es un valor númerico
        return ("Error 3")  # se retorna el Error 3 si sentence no es un string
    for i in sentence:  # se hace un recorrido para contar los caracteres
        count = count + 1  # se suma una unidad por cada caracter
    return (count)  # se retorna la suma total de caracteres
