Nombre_completo = input("Ingrese su nombre completo: " )

dni = input("Ingrse su dni: ")
if len("dni") > 8 and len("dni"< 8):
    print("Dni incorrecto")
edad = input("Ingrese su edad: ")
tiene_obra_social = input("tiene obra social?(si/no): ").lower
prioridad_medica = int(input("nivel prioridad (1) = emergencia, (2) = urgente (3) = control: "))
guardia = False
print(f"Paciente: \t {Nombre_completo}")
print (f"DNI:\t \t {dni}")
print (f"Edad: \t \t {edad}")
print (f"Prioridad: \t {prioridad_medica}")

if prioridad_medica == 1:
    print("Redirigir a guardia ")
elif prioridad_medica == 2 and tiene_obra_social == "si":
        print("Su turno es dentro de 24 hs")
else:
        print("Turno asignado:\t en 48 hs")
if prioridad_medica == 3:
    if edad > "65":
        print("Turno asignado:\t en 72 horas") 
    elif edad < "65":
        print("Turno asignado:\t en 7 dias")


