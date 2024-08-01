from flask import Flask, request, jsonify
from flask_restful import Api
from models.gato import Gato
from models.perro import Perro
from models.boa_constrictor import Boa_Constrictor
from models.huron import Huron

#Cargar configuración de la base de datos
app = Flask(__name__)
api = Api(app)

#Pantalla de inicio
@app.route("/animales/hacer-sonido")
def hacer_sonido():
    cedula = request.args.get('cedula')
    animal = request.args.get('animal')

    sonido = ""

    #Dependiendo del ultimo digito de la cedula se hace el sonido
    #Tiene prioridad el parametro numero de cedula sobre el parametro animal
    if cedula != None:
        digito_cedula = int(cedula[-1])
        if digito_cedula >= 0 and digito_cedula <= 3:
            animal = "gato"
        elif digito_cedula >= 4 and digito_cedula <= 6:
            animal = "huron"
        else:
            animal = "boa-constrictor"
    
    #De acuerdo al tipo de animal obtiene el sonido
    match animal:
        case "gato":
            sonido = Gato().hacer_sonido()
        case "perro":
            sonido = Perro().hacer_sonido()
        case "boa-constrictor":
            sonido = Boa_Constrictor().hacer_sonido()
        case "huron":
            sonido = Huron().hacer_sonido()
        case _:
            sonido = "El animal enviado no tiene un sonido establecido en la api."

    data = {
        'response': sonido
    }

    #Convertir el diccionario a JSON con jsonify
    json_data = jsonify(data)

    #Return JSON de respuesta
    return json_data

@app.route("/")
def welcome():
    return 'welcome'

if __name__ == '__main__':
    app.run(debug=True)