for _ in range(10):
    try:
        num1 = int(input("Inserta un numero: "))
        num2 = int(input("Inserta un numero: "))
        suma = num1 + num2 
        print(f"La suma es: {suma}")
    except Exception as error:
        print(f"No has insertado unos datos validos. Error: {error}")
    print("Accion realizada")