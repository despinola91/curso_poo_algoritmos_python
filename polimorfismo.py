class Persona:

    def __init__(self, nombre):
        self.nombre = nombre


    def avanza(self):
        print(f"Me llamo {self.nombre} y ando caminando.")


class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print(f"Me llamo {self.nombre} y ando pedaleando.")

if __name__ == "__main__":
    persona = Persona("Carlos")
    persona.avanza()

    ciclista = Ciclista("Mariano")
    ciclista.avanza()
