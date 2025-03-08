from pathlib import Path

ruta = Path(r'D:\Música\Post-Punk Rusian\post punk ruso')

# Listamos los elementos
for elemento in ruta.iterdir():
    if elemento.is_file():
        print(f"Archivos: {elemento.name}")