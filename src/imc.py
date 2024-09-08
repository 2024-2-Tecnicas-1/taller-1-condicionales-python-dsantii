def evaluar(peso, estatura, edad):
    # TODO: Coloca aquí el código del ejercicio 8: Índice de masa corporal
    imc = peso / (estatura ** 2)
    
    
    if imc < 18.5:
        clasificacion = "Bajo peso"
    elif 18.5 <= imc < 24.9:
        clasificacion = "Peso normal"
    elif 25 <= imc < 29.9:
        clasificacion = "Sobrepeso"
    else:
        clasificacion = "Obesidad"
    
    
    respuesta = f"IMC: {imc:.2f}\nClasificación: {clasificacion}"
    
    return respuesta

if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
