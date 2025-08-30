#3) hacer mas tarde cuando sepa usar el utiles_es
#4)El programa debe calcular el impuesto anual que debe pagar una persona en función de sus ingresos y edad:


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