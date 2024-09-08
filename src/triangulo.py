def evaluar(a, b, c):
    # TODO: Coloca aquí el código del ejercicio 1: Set de tenis
    
    if a >= 6 and a - b >= 2:
        respuesta = "Jugador A ganó el set"
    elif b >= 6 and b - a >= 2:
        respuesta = "Jugador B ganó el set"
    elif c >= 6 and c - a >= 2 and c - b >= 2:
        respuesta = "Jugador C ganó el set"
    else:
        respuesta = "El set aún no ha terminado"
    
    return respuesta
    

if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)
