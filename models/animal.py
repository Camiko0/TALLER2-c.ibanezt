from models.ianimal import iAnimal
from abc import ABC, abstractmethod

#Clase animal que implementa de iAnimal con metodo abstracto
class Animal(iAnimal, ABC):
    def __init__(self, nombre: str, peso: float, edad: int) -> None:
        self._nombre = nombre
        self._peso = peso
        self._edad = edad
        self._kilos_comidos = 0

    # Metodos abstactos
    @abstractmethod
    def hacer_sonido(self) -> str:
        pass
    
    # Metodos implementados
    def comer(self, kilos: float) -> None:
        self._kilos_comidos += kilos

    def obtener_kilos_comidos(self) -> float:
        return self._kilos_comidos
    
    # Getters
    def obtener_nombre(self) -> str:
        return self._nombre
    
    def obtener_peso(self) -> float:
        return self._peso
    
    def obtener_edad(self) -> int:
        return self._edad
    
    # Otros metodos
    def obtener_informacion(self) -> str:
        return "Nombre: {}. Peso: {}. Edad: {}".format(self.obtener_nombre(), self.obtener_peso(), self.obtener_edad())