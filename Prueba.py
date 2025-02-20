# Número secreto
secreto = 7
intento = 0  # Variable para almacenar el intento del usuario

# Mientras el intento no sea igual al número secreto
while intento != secreto:
    intento = int(input("Adivina el número (entre 1 y 10): "))
    
    if intento == secreto:
        print("¡Felicidades! Adivinaste el número.")
    else:
        print("Incorrecto, intenta de nuevo.")
