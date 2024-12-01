# Definición de la clase Cotxe
class Cotxe:
    def __init__(self, matricula, num_rodes, portes, kilometraje, color):
        self.matricula = matricula
        self.num_rodes = num_rodes
        self.portes = portes
        self.kilometraje = kilometraje
        self.color = color

    # Métodos getters
    def getMatricula(self):
        return self.matricula

    def getNumRodes(self):
        return self.num_rodes

    def getPortes(self):
        return self.portes

    def getKilometraje(self):
        return self.kilometraje

    def getColor(self):
        return self.color

    # Métodos setters
    def setKilometraje(self, kilometraje):
        self.kilometraje = kilometraje

    def setColor(self, color):
        self.color = color


# Definición de la clase Colibri
class Colibri:
    def __init__(self, nombre, edad, color, altura, velocidad):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.altura = altura
        self.velocidad = velocidad

    # Métodos getters
    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getColor(self):
        return self.color

    def getAltura(self):
        return self.altura

    def getVelocidad(self):
        return self.velocidad

    # Métodos setters
    def setEdad(self, edad):
        self.edad = edad

    def setVelocidad(self, velocidad):
        self.velocidad = velocidad


# Bloque principal
if __name__ == "__main__":
    # Instancias de la clase Cotxe
    cotxe_1 = Cotxe("1234ABC", 4, 5, 15000, "Rojo")
    cotxe_2 = Cotxe("5678XYZ", 4, 5, 20000, "Azul")
    cotxe_3 = Cotxe("91011DEF", 4, 5, 10000, "Verde")

    # Instancias de la clase Colibrí
    colibri_1 = Colibri("Colibrí 1", 2, "Verde", 0.5, 20)
    colibri_2 = Colibri("Colibrí 2", 1, "Amarillo", 0.6, 22)
    colibri_3 = Colibri("Colibrí 3", 3, "Rojo", 0.4, 18)

    # Mostrar 3 getters de Cotxe
    print(f"Matricula de Cotxe 1: {cotxe_1.getMatricula()}")
    print(f"Numero de ruedas de Cotxe 1: {cotxe_1.getNumRodes()}")
    print(f"Color de Cotxe 1: {cotxe_1.getColor()}\n")

    # Mostrar 4 getters de Colibrí
    print(f"Nombre de Colibrí 1: {colibri_1.getNombre()}")
    print(f"Edad de Colibrí 1: {colibri_1.getEdad()}")
    print(f"Color de Colibrí 1: {colibri_1.getColor()}")
    print(f"Altura de Colibrí 1: {colibri_1.getAltura()}\n")

    # Modificar 2 atributos de Cotxe mediante setters
    cotxe_1.setKilometraje(16000)  # Modificamos kilometraje
    cotxe_1.setColor("Negro")  # Modificamos color

    # Mostrar los 2 atributos modificados de Cotxe
    print(f"Nuevo kilometraje de Cotxe 1: {cotxe_1.getKilometraje()}")
    print(f"Nuevo color de Cotxe 1: {cotxe_1.getColor()}\n")

    # Modificar 2 atributos de Colibrí mediante setters
    colibri_1.setEdad(3)  # Modificamos edad
    colibri_1.setVelocidad(25)  # Modificamos velocidad

    # Mostrar los 2 atributos modificados de Colibrí
    print(f"Nuevo edad de Colibrí 1: {colibri_1.getEdad()}")
    print(f"Nueva velocidad de Colibrí 1: {colibri_1.getVelocidad()}")
