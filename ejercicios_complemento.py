#ejercicio 1 sistemas de becas estudiantiles 
nombre_completo = input("ingrese su nombre completo: ")
edad = int(input("Ingrese su edad: "))
promedio = float(input("Ingrese su promedio: "))
while promedio > 10:
    promedio = float(input("Ingrese su promedio menor o igual a 10: "))
ingresos_mensuales = int(input("Ingrese sus ingresos mensuales: "))
if promedio < 6:
    Beca = "Beca rechazada"
elif promedio >=6 and promedio <= 10:
    if ingresos_mensuales <= 300000:
        Beca = "Beca completa"
    elif ingresos_mensuales <= 600000:
        Beca = "Beca parcial"
    elif ingresos_mensuales >= 600000:
        Beca = "Beca rechazada"
print(f"{nombre_completo}, {edad} ")
print(f"Promedio:\t{promedio}")
print(f"Ingresos:\t{ingresos_mensuales}")
print(f"Resultado:\t{Beca}")
print ("\n")
#2) Gestion de turnos hospitalarios
print ("\n")
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
print ("\n")
#ejercicios de condicionales
#1)El programa debe calcular el impuesto anual que debe pagar una persona en función de sus ingresos y edad:
print ("\n")
nombre_completo = input("Ingrese su nombre completo: ")
edad =  int(input("ingrese su edad: "))
ingresos_anuales =  int(input("Introduzca sus ingresos anuales (sin decimales ni puntos): "))
if ingresos_anuales < 500000:
	impuestos =0
elif ingresos_anuales <= 2000000:
	impuestos = 0.1
elif ingresos_anuales <5000000:
	impuestos = 0.2
elif ingresos_anuales >= 5000000:
	impuestos = 0.35
if edad > 65:
	impuestos = impuestos * 0.5	
impuestos_reales = round(ingresos_anuales * impuestos, 2)
print (f"Nombre:\t \t \t {nombre_completo}")
print (f"Ingresos anuales:\t {ingresos_anuales}")
print (f"Edad:\t \t\t {edad}")
print (f"Impuestos:\t \t {impuestos_reales}")
#2)Sistema de calificaciones con promoción
condicion = 0
nombre_completo = input("Introduce tu nombre completo: ")
legajo = input("Ingrese su numero de legajo(un legajo tiene 8 digitos): ")
while condicion == 0:
	largo = len(legajo)
	if largo >8 or largo <8:
		legajo = int(input("Ingrese su numero de legajo: "))
	elif largo <=8 and largo >=1:
		condicion = 1
aprobado = True
i = 0
promedio = 0
while i <3:
	i = i + 1
	nota = int(input("Ingrese una nota entre 0-10: "))
	if nota >10 or nota < 0:
		nota = 0
		i = i -1
	if nota < 4:
		aprobado = False
	promedio = promedio + nota
promedio = round(promedio / 3,2)
if aprobado == True:
	if promedio < 6:
		estado_academico = "Desaprobado" 
	elif promedio >= 6 and promedio <8:
		estado_academico = "Aprobado con final"
	else:
		estado_academico = "Promocionado"
else:
	estado_academico = "Desaprobado directo"
print("\n")
print(f"identidad:\t\t{nombre_completo}, {legajo} ")
print(f"Promedio:\t\t{promedio}")
print(f"Estado academico :\t{estado_academico}")
print ("\n")
