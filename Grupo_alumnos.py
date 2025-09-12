import random
#lista alumnos
alumnos = ["Valentina De Los ángeles Albizú","Pablo Andres Allende","Luca Valentín Argumedo","Pablo Avalos","Lucas Avila","Santino Barone","Sofia Blangetti","Nicolás Bohm","Renzo Valentino Borello Canizo","Juan Manuel Carrillo Taglio","Facundo Gustavo Chacon Catalan","Agustin Emiliano Contardi",
"Jeronimo Coronel Alvarez","Gabriel Emiliano Denis","Facundo Gustavo Deseff","Juan Martin García","Enzo Giaquinta","Sabrina Gimenez","Joaquin Godoy",
"Lucas Facundo Godoy","Santino Alejo Godoy Galdeano","Valentina Antonela Gordillo Moreno","Lautaro Agustin Guardatti Esquivel","Tiago Nahuel Guillot Duran","Mateo Lautaro Liendo","Juan Ignacio Martinez Quiroga","Maximo Exequiel Monardez","Tomas Agustin Mora Gonzalez","Pablo Isaias Morinigo Lima","Ares Martín Ocaña Martinez","Thiago Santino Oviedo Saldaño",
"Amanda Lucrecia Pagano","Máximo Juan Cruz Quiroga","Facundo Agustín Ramírez García","Franco Agustin Rios Alzamora","Leonel Enrique Rojas","Matias Nicolas Ruiz Vargas","Ramiro Ezequiel Salcedo","Ismael Saleme Padolsky","Ignacio Exequiel Sanchez","Fabrizio Jonathan Simon Santos",
"Cristian Gabriel Soto","Giovanna Mercedes Suarez","Ismael Mauricio Suarez","Fernando Agustín Torrez","Luca Nicolas Valdez","Tiziano Ignacio Valentini","Matias Nicolas Vargas","Juan Ignacio Videla Continella","Pablo Exequiel Avalos"]
cantidad_alumnos = len(alumnos)
cantidad_filas = round(cantidad_alumnos/4)
num = random.sample(range(0,cantidad_alumnos),cantidad_alumnos)
columnas = 12
filas = 4
grupos_matriz= [[0 for _ in range(filas)]for _ in range(columnas)]
contador = 0
for colum in range(columnas):
    for fila in range(filas):
        if contador < cantidad_alumnos:
            grupos_matriz[colum][fila] = alumnos[num[contador]]
            contador += 1
for colum in range(columnas):
    print(grupos_matriz[colum],"\n")