# acessoBD.py
import json
from apiPostgre import ConexaoBD
from datetime import date

class Estacoes:

    def getAll(self):
        sql="""SELECT * FROM \"estacoes\" """
        conexao=ConexaoBD()
        resposta=conexao.consulta(sql)
        return(resposta)
    def getByID(self,idEstacao):
        sql=("SELECT * FROM \"estacoes\" WHERE id=%s",(idEstacao))
        conexao=ConexaoBD()
        resposta=conexao.consulta(sql)
        return(resposta)
       
        

class Laboratorios:
    pass

class MedLabProg:
    def getAll(self):
        sql="""SELECT * FROM \"med_labprog\" """
        return(self.getResultado(sql))

    def getByInterval(self,dataInicio,dataFim):
        # SELECT * FROM med_labsoft WHERE time BETWEEN '2019-02-20' AND '2019-02-21'
        sql="SELECT * FROM \"med_labprog\" WHERE time BETWEEN \'"+dataInicio+ "\' AND \'"+dataFim+"\'"
        return(self.getResultado(sql))
        
    
    def getByDay(self,data):
        sql="SELECT date_trunc('day', time)::date as nData,sum(total),sum(iluminacao),sum(rede),sum(ar_cond),sum(bancadas) FROM med_labprog WHERE date_trunc('day', time)=\'"+data+"\' GROUP BY  date_trunc('day', time) ORDER BY nData; "
        return(self.getResultado(sql))

    def getByMonthDays(self,mes):
        sql="SELECT date_trunc('day', time)::date as nData,sum(total),sum(iluminacao),sum(rede),sum(ar_cond),sum(bancadas) FROM med_labprog WHERE extract(MONTH FROM time)=2 GROUP BY  nData ORDER BY  nData;"
        return(self.getResultado(sql))

    def getByMonth(self,mes):
        sql="SELECT extract(MONTH FROM time) as mes,sum(total),sum(iluminacao),sum(rede),sum(ar_cond),sum(bancadas) FROM med_labprog WHERE extract(MONTH FROM time)="+mes+" GROUP BY mes ORDER BY mes;"
        return(self.getResultado(sql))

    def getByYearMonths(self,ano):
        sql="SELECT (extract(YEAR FROM time) ||'-'|| extract(MONTH FROM time)) as nData,sum(total),sum(iluminacao),sum(servidor),sum(rede),sum(ar_cond),sum(bancadas) FROM med_labprog WHERE extract(YEAR FROM time)="+ ano +" GROUP BY  nData ORDER BY  nData;"
        return(self.getResultado(sql))

    def getByYear(self,ano):
        sql="SELECT extract(YEAR FROM time) as ano,sum(total),sum(iluminacao),sum(rede),sum(ar_cond),sum(bancadas) FROM med_labprog WHERE extract(YEAR FROM time)="+ ano +" GROUP BY ano ORDER BY ano;"
        return(self.getResultado(sql))

    def getResultado(self,sql):
        conexao=ConexaoBD()
        resposta=conexao.consulta(sql)
        return(resposta)


#-----------------------------------------------------------------------------------------------------------------------



class MedLabSoft:
    def getAll(self):
        sql="""SELECT * FROM \"med_labsoft\" """
        return(self.getResultado(sql))

    def getByInterval(self,dataInicio,dataFim):
        # SELECT * FROM med_labsoft WHERE time BETWEEN '2019-02-20' AND '2019-02-21'
        sql="SELECT * FROM \"med_labsoft\" WHERE time BETWEEN \'"+dataInicio+ "\' AND \'"+dataFim+"\'"
        return(self.getResultado(sql))
        
    
    def getByDay(self,data):
        sql="SELECT date_trunc('day', time)::date as nData,sum(total),sum(iluminacao),sum(rede),sum(ar_cond),sum(bancadas),sum(servidor) FROM med_labsoft WHERE date_trunc('day', time)=\'"+data+"\' GROUP BY  date_trunc('day', time) ORDER BY nData; "
        return(self.getResultado(sql))

    def getByMonthDays(self,mes):
        sql="SELECT date_trunc('day', time)::date as nData,sum(total),sum(iluminacao),sum(rede),sum(ar_cond),sum(bancadas),sum(servidor) FROM med_labsoft WHERE extract(MONTH FROM time)=2 GROUP BY  nData ORDER BY  nData;"
        return(self.getResultado(sql))

    def getByMonth(self,mes):
        sql="SELECT extract(MONTH FROM time) as mes,sum(total),sum(iluminacao),sum(rede),sum(ar_cond),sum(bancadas),sum(servidor) FROM med_labsoft WHERE extract(MONTH FROM time)="+mes+" GROUP BY mes ORDER BY mes;"
        return(self.getResultado(sql))

    def getByYearMonths(self,ano):
        sql="SELECT (extract(YEAR FROM time) ||'-'|| extract(MONTH FROM time)) as nData,sum(total),sum(iluminacao),sum(rede),sum(ar_cond),sum(bancadas),sum(servidor) FROM med_labsoft WHERE extract(YEAR FROM time)="+ ano +" GROUP BY  nData ORDER BY  nData;"
        return(self.getResultado(sql))

    def getByYear(self,ano):
        sql="SELECT extract(YEAR FROM time) as ano,sum(total),sum(iluminacao),sum(rede),sum(ar_cond),sum(bancadas),sum(servidor) FROM med_labsoft WHERE extract(YEAR FROM time)="+ ano +" GROUP BY ano ORDER BY ano;"
        return(self.getResultado(sql))

    def getResultado(self,sql):
        conexao=ConexaoBD()
        resposta=conexao.consulta(sql)
        return(resposta)
    

    def tratamentoDados(self,dados,filtro=""):
        lista=[]
        for item in dados:            
            # dia=str(item[0].day)
            # mes=str(item[0].month)
            # ano=str(item[0].year)
            #hora=str(item[0].hour)
            #minuto=str(item[0].minute)

            dado={}
            dado={  "data":item[0],
                    #"horario":hora+":"+minuto,
                    "consumoTotal":item[1],
                    "iluminacao":item[2],
                    "servidor":item[3],
                    "rede":item[4],
                    "arCond":item[5],
                    "bancadas":item[6]
            }
            lista.append(dado)
            resultado={"lista":lista}
        return(resultado)

#-----------------------------------------------------------------------------------------------------------------------

class Metricas:
    pass
#-----------------------------------------------------------------------------------------------------------------------

class acessoBD:

    colunas=("Total","iluminacao","rede","ar_cond","bancadas","servidor")

    def consumoMensal(self,mes=str(date.today().month)):
        mediLabSoft=MedLabSoft()
        mediLabProg=MedLabProg()

        listaLabSoft=mediLabSoft.getByMonth(mes)
        listaLabProg=mediLabProg.getByMonth(mes)

        ls,lp=self.consumo(listaLabSoft,listaLabProg)

        dados={ "mes":mes,
                "labSoft": ls,
                "labProg":lp
        }

        # return(json.dumps(dados))
        return(dados)

    def consumoAnual(self,ano=str(date.today().year)):
        mediLabSoft=MedLabSoft()
        mediLabProg=MedLabProg()

        listaLabSoft=mediLabSoft.getByYear(ano)
        listaLabProg=mediLabProg.getByYear(ano)

        ls,lp=self.consumo(listaLabSoft,listaLabProg)

        dados={ "ano":ano,
                "labSoft": ls,
                "labProg":lp
        }

        # return(json.dumps(dados))
        return(dados)

    def consumo(self,listaS,listaP):
        
        listaSoft= []

        for item in listaS:
            dado={}
            
            for a in range(1,len(self.__class__.colunas)):
                consumo=round(item[a]/1000,2) #kW
                gasto=round(consumo*0.4836,2)
                dado={  "nome": self.__class__.colunas[a-1],
                        "consumo":str(consumo),
                        "gasto": str(gasto)
                }
                listaSoft.append(dado)
            


        i=0
        listaProg= []
        for item in listaP:
            dado={}
            for b in range(1,len(self.__class__.colunas)-1):
                consumo=round(item[b]/1000,2) #kW
                gasto=round(consumo*0.4836,2)
                dado={  "nome":self.__class__.colunas[b-1],
                        "consumo":str(consumo),
                        "gasto": str(gasto)
                }
                listaProg.append(dado)
        
        return(listaSoft,listaProg)
        

if (__name__=="__main__"):
    # mediLabSoft=MedLabSoft()
    # teste=mediLabSoft.getByMonthDays('02')
    # lista=mediLabSoft.tratamentoDados(teste)
    # for item in lista["lista"]:
    #     print(item)

    a=acessoBD()
    print(a.consumoAnual())

    # tarifa: R$0,4836 o KWh

    # SELECT sum(total),sum(iluminacao),sum(servidor),sum(rede),sum(ar_cond),sum(bancadas) FROM med_labsoft WHERE time BETWEEN '2019-02-20' AND '2019-02-21' GROUP BY  DATE_PART('MONTH', time)

    # SELECT date_trunc('day', time)::date as nData,sum(total),sum(iluminacao),sum(servidor),sum(rede),sum(ar_cond),sum(bancadas) FROM med_labsoft WHERE time BETWEEN '2019-02-20' AND '2019-04-01' GROUP BY  date_trunc('day', time) ORDER BY nData; 