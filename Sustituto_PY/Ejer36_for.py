def Tabla_Multiplicar(num_tabla: int):
    resultado = None
    i= 0
    for i in range(0, 10):
        i = i + 1
        resultado= i*num_tabla
        print(f"{num_tabla} x {i} = {resultado}")
num_tabla = int(input("Introduzca el numero de tabla"))
Tabla_Multiplicar(num_tabla)