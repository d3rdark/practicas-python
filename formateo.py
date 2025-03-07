# Formatear integers y floats con la anchura y precisión especificadas
print("Número de paquetes comprados : {0:2d}, precio total : ${1:8.2f}".format(12,12 * 150.58))

# buscar si una palabra comienza con cierta letra o letras
palabra = "Hola"
if palabra.startswith('Ho'):
    print('Si comienza con Ho')
    

#En base al número de control hacer una busqueda con la sub cadena para encontrar de que año es
num_Control = "181G0251"

if num_Control[0:4].__contains__('181G'):
    print('El numero de control es del año 2018')
else:
    print('El numero de control es de otro año')