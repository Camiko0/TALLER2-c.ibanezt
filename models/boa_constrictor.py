from models.animal_exotico import Animal_Exotico

#Clase Boa_Constrictor que implementa de Animal_Exotico con los metodos abstractos implementados
class Boa_Constrictor(Animal_Exotico):
    def __init__(self) -> None:
        self._nombre = ""

    # Metodos implementados
    def hacer_sonido(self) -> str:
        return "Tsss!"
    
    # Otros metodos
    def obtener_ratones_comidos(self) -> int:
        return self.__ratones_comidos
    
    def sumar_ratones_comidos(self, ratones: int) -> None:
        if self.__ratones_comidos == 20:
            return ValueError("La boa está llena")
        self.__ratones_comidos += ratones
        return "Éxito"