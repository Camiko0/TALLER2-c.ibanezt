from abc import ABC, abstractmethod

#Clase iAnimal con sus metodos abstractos
class iAnimal(ABC):
    # Metodos abstactos
    @abstractmethod
    def comer(self, kilos: float) -> None:
        pass

    @abstractmethod
    def obtener_kilos_comidos(self) -> float:
        pass