import math
def line():
    A = (float(input("")))
    B = (float(input("")))
    X1 = (float(input("")))
    X2 = (float(input("")))
    Y1 = (float(A * X1) + B)
    Y2 = (float(A * X2) + B)

    print(f"El coeficiente A de su ecuación de la recta es: {A}")
    print(f"El coeficiente B de su ecuación de la recta es: {B}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {X2}\n")

    print("Para la siguiente ecuación:")
    print(f"\tY = {A}X + {B}\n")
    print("Dados los siguientes puntos:")
    print(f"\tP1 ({X1}, {Y1})")
    print(f"\tP2 ({X2}, {Y2})\n")
    print(f"La distancia entre ellos es: {math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)}")
