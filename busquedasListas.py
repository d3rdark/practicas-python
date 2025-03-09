class Alumno:
    def __init__(self, Control, Paterno, Materno, Nombre, Sexo, Carrera, Entrada):
        self.Control = Control
        self.Paterno = Paterno
        self.Materno = Materno
        self.Nombre = Nombre
        self.Sexo = Sexo
        self.Carrera = Carrera
        self.Entrada = Entrada


def llenar_alumnos():
    alumnos = []
    alumnos.append(Alumno(Control="001G0077", Paterno="DE LEON", Materno="TREJO", 
                        Nombre="ELSA GEORGINA ", Sexo=2, Carrera="G", Entrada=2000))
    return alumnos


if __name__ == "__main__":
    lista_Completa = llenar_alumnos()
    print("=== BASE DE DATOS DE ALUMNOS ===")
    print(f"Total de registros: {len(lista_Completa)}")
    print("\nPrimer registro:")
    primer_alumno = lista_Completa[0]
    print(f"Numero de control = {primer_alumno.Control}")
    print(f"Nombre del alumno = {primer_alumno.Nombre}")