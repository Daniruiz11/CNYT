'LIBRERÍA DE COMPUTACIÓN CUÁNTICA'
'Calculadora de Números Complejos'
import math

'-----------------------------------Operaciones Básicas-----------------------------------'

def adicionar(complejo1, complejo2):
    parte_real = complejo1[0] + complejo2[0]
    parte_imaginaria = complejo1[1] + complejo2[1]
    return(parte_real, parte_imaginaria)

def sustraer(complejo1, complejo2):
    parte_real = complejo1[0] - complejo2[0]
    parte_imaginaria = complejo1[1] - complejo2[1]
    return(parte_real, parte_imaginaria)

def multiplicar(complejo1, complejo2):
    parte_real = (complejo1[0] * complejo2[0]) - (complejo1[1] * complejo2[1])
    parte_imaginaria = (complejo1[0] * complejo2[1]) + (complejo1[1] * complejo2[0])
    return(parte_real, parte_imaginaria)

def conjugado(complejo):
    return(complejo[0], -1 * complejo[1])

def magnitud(complejo):
    return math.sqrt(complejo[0]**2 + complejo[1]**2)

def dividir(complejo1, complejo2):
    if complejo2[0] == 0 and complejo2[1] == 0:
        raise ValueError('¡No es posible dividir por cero!')
    else:
        denominador = complejo2[0]**2 + complejo2[1]**2
        parte_real = (complejo1[0] * complejo2[0]) + (complejo1[1] * complejo2[1])
        parte_imaginaria = (complejo1[1] * complejo2[0]) - (complejo1[0] * complejo2[1])
        return(parte_real / denominador, parte_imaginaria / denominador)

def polar_a_cartesiano(coord_polar):
    parte_real = coord_polar[0] * math.cos(coord_polar[1])
    parte_imaginaria = coord_polar[0] * math.sin(coord_polar[1])
    return(parte_real, parte_imaginaria)

def cartesiano_a_polar(coord_cartesiana):
    magnitud = math.sqrt(coord_cartesiana[0]**2 + coord_cartesiana[1]**2)
    angulo = fase(coord_cartesiana)
    return(magnitud, angulo)

def fase(complejo):
    angulo_rad = math.atan2(complejo[1], complejo[0])
    return(math.degrees(angulo_rad) % 360)
