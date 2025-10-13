try:
    with open("C:\\Users\\galle\\Downloads\\listaAlumnosC4.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            nombre = linea_limpia.strip(";")
            print(nombre ,"\n" )
except FileNotFoundError:
    print("Error no se encontro el archivo")
except Exception as E:
    print(f"ocurrio un error inesperado: {e}")