from persona import Persona
from deportista import Deportista


class Futbolista(Persona, Deportista):
    _listaFutbolistas = []

    def __init__(self, nombre="", edad=0, altura=0, sexo="M", años=0, goles=0, tarjetas=0, pierna=""):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, años)
        self._golesMarcados = goles
        self._tarjetasRojas = tarjetas
        self._piernaHabil = pierna
        Futbolista._listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados

    def setGolesMarcados(self, goles):
        self._golesMarcados = goles

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setTarjetasRojas(self, tarjetas):
        self._tarjetasRojas = tarjetas

    def getPiernaHabil(self):
        return self._piernaHabil

    def setPiernaHabil(self, pierna):
        self._piernaHabil = pierna

    @classmethod
    def getListaFutbolistas(self):
        return Futbolista._listaFutbolistas

    @classmethod
    def setListaFutbolistas(self, lista):
        Futbolista._listaFutbolistas = lista

    def __str__(self):
        return f"Mi nombre es {self.getNombre} soy profesional en el deporte {self.getDeporte} Tengo {self.getEdad} años de edad y llevo {self.getAñosPracticando} años en el deporte"
