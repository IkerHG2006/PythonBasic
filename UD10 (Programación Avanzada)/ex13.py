from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    @abstractmethod
    def xerrar(self):
        pass

    @abstractmethod
    def mourem(self):
        pass

    def quisoc(self):
        return f"Soy un {self.especie} de {self.edad} años."

class Cavall(Animal):
    def xerrar(self):
        return "Hiii"

    def mourem(self):
        return "Galopando"

class Dofí(Animal):
    def xerrar(self):
        return "Cliiic"

    def mourem(self):
        return "Nadando"

class Abella(Animal):
    def xerrar(self):
        return "Bzzz"

    def mourem(self):
        return "Volando"

    def picar(self):
        return "¡He picado!"

class Humà(Animal):
    def __init__(self, especie, edad, nom):
        super().__init__(especie, edad)
        self.nom = nom

    def xerrar(self):
        return "Hola"

    def mourem(self):
        return "Caminando"

class Fiet(Humà):
    def __init__(self, especie, edad, nom, pares):
        super().__init__(especie, edad, nom)
        self.pares = pares

    def nompares(self):
        return f"Mis padres son: {', '.join(self.pares)}"

class Centaure(Cavall, Humà):
    def __init__(self, especie, edad, nom):
        Cavall.__init__(self, especie, edad)
        Humà.__init__(self, especie, edad, nom)

class Xou:
    def xerrar(self):
        return "Xouuuu"

    def mourem(self):
        return "Espectáculo"

animales = [
    Cavall("Cavall", 5),
    Dofí("Dofí", 3),
    Abella("Abella", 1),
    Humà("Humà", 30, "Juan"),
    Fiet("Fiet", 10, "Anna", ["María", "Carlos"]),
    Centaure("Centaure", 25, "Hércules"),
    Xou()
]

for animal in animales:
    print(animal.xerrar(), animal.mourem())