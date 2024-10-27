peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu estatura en metros: "))

imc = peso / (altura ** 2)

print("Tu índice de masa corporal es", round(imc, 2))
