def evaluar(caracter):
    # TODO: Coloca aquí el código del ejercicio 4: Letra o número
    if caracter.isalpha():
        if caracter.isupper():
            respuesta = "Es letra mayúscula"
        else:
            respuesta = "Es letra minúscula"
    
    elif caracter.isdigit():
        respuesta = "Es número"
    
    else:
        respuesta = "No es letra ni número"
    

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
