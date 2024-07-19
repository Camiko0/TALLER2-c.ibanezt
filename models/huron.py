from models.animal_exotico import Animal_Exotico

#Clase Huron que implementa de Animal_Exotico con los metodos abstractos implementados
class Huron(Animal_Exotico):
    def __init__(self) -> None:
        self._nombre = ""

    # Metodos implementados
    def hacer_sonido(self) -> str:
        return "¡Eek Eek!"