from datetime import date


def evaluar(dia, mes, anno):
    # TODO: Coloca aquí el código del ejercicio 6: Edad
    hoy = date.today()
    
    
    edad = hoy.year - anno
    
    
    if (hoy.month, hoy.day) < (mes, dia):
        edad -= 1
    
    
    respuesta = "Usted tiene " + str(edad) + " años"
    return respuesta
    

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
