# hacer un algoritmo de matricula ABC 123
abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
largo = len(abecedario)
contador = 0
repeticion = int(input("Que numero de matriucla vas a generar? "))
for i in range(0,largo):
    for j in range(0,largo):
        for k in range(0,largo):
            for x in range(0,10):
                for y in range(0,10):
                    for z in range(0,10):
                        contador += 1
                        if contador == repeticion:
                            print(f"Matricula: {abecedario[i]}{abecedario[j]}{abecedario[k]}{x}{y}{z}")
                            break