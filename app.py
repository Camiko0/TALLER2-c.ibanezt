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
    animal = request.args.get('animal')

    sonido = ""
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

if __name__ == '__main__':
    app.run(debug=True)