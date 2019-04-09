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

class ConsumoAnualDetalhado(Resource):
    def get(self,ano=""):
        acBD=acessoBD()
        if(ano==""):         
            return (acBD.consumoAnualDetalhado())
        else:
            return (acBD.consumoAnualDetalhado(ano))
            


class ConsumoMensal(Resource):
    def get(self,mes="",ano=""):        
        acBD=acessoBD()
        if(mes==""):
            return (acBD.consumoMensal())
        elif(ano==""):
            return (acBD.consumoMensal(mes))
        else:
            return (acBD.consumoMensal(mes,ano))

class ConsumoMensalDetalhado(Resource):
    def get(self,mes="",ano=""):        
        acBD=acessoBD()
        if(mes==""):
            return (acBD.consumoMensalDetalhado())
        elif(ano==""):
            return (acBD.consumoMensalDetalhado(mes))
        else:
            return (acBD.consumoMensal(mes,ano))

class Inicio(Resource):
    def get(self):
        return ("Inicio")




api.add_resource(Inicio, '/')
api.add_resource(ConsumoAnual, '/consumoAnual')
api.add_resource(ConsumoMensal, '/consumoMensal')
api.add_resource(ConsumoAnualDetalhado, '/consumoAnualDet')
api.add_resource(ConsumoMensalDetalhado, '/consumoMensalDet')



# @app.route("/")
# def home():
#     return "Hello, A!"

# @app.route("/diego")
# def Diego():
#     return "Diego"


if __name__ == '__main__':
    app.run(debug=True)
