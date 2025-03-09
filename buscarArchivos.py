from pathlib import Path

def crearTxtDeArchivos(ruta):
    ruta_padre = Path(rf"{ruta}")
    extensiones_validas = {'.mp3', '.flac'}
    opcionUsuario = input("Quieres crear un archivo .txt con el\nnombre de los archivos o solo quieres ver los archivos? (S/N): ")
    
    match opcionUsuario:
        case "S":
            print("Se esta creando el archivo de texto con el nombre de los archivos")
            for archivos in ruta_padre.glob('*'):
                if archivos.is_file() and archivos.suffix.lower() in extensiones_validas:
                    print(archivos.name)
                
        case "N":
            print("No se ha creado el archivo")
# D:\Música\Post-Punk Rusian\post punk ruso
ruta_padre = input("Dame la ruta donde quieres ver los archuivos: ")
crearTxtDeArchivos(ruta_padre)