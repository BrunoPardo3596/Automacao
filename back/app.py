from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from acessoBD import acessoBD

app=Flask(__name__)
api = Api(app)

class ConsumoAnual(Resource):
    def get(self,ano=""):
        acBD=acessoBD()
        if(ano==""):            
            return (acBD.consumoAnual())
        else:
            return (acBD.consumoAnual(ano))
            


class ConsumoMensal(Resource):
    def get(self,mes=""):        
        acBD=acessoBD()
        if(mes==""):
            return (acBD.consumoMensal())
        else:
            return (acBD.consumoMensal(mes))

class Inicio(Resource):
    def get(self):
        return ("Inicio")




api.add_resource(Inicio, '/')
api.add_resource(ConsumoAnual, '/consumoAnual')
api.add_resource(ConsumoMensal, '/consumoMensal')




# @app.route("/")
# def home():
#     return "Hello, A!"

# @app.route("/diego")
# def Diego():
#     return "Diego"


if __name__ == '__main__':
    app.run(debug=True)
