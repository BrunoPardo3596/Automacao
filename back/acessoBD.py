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
    sqlSelect=""
    
    sqlBase= """
        ,sum(subconsulta.iluminacao) as iluminacao,
        sum(subconsulta.rede) as rede,
        sum(subconsulta.ar) as ar,
        sum(subconsulta.bancada) as bancada
		FROM (SELECT time_bucket('01:00:00'::interval, filtro."time") AS hora,
				avg(filtro.consumo_total::numeric * 0.001) AS por_hora,	  
                avg(filtro.iluminacao::numeric * 0.001) AS iluminacao,
                avg(filtro.rede::numeric * 0.001) AS rede,
                avg(filtro.ar_cond::numeric * 0.001) AS ar,
                avg(filtro.bancadas::numeric * 0.001) AS bancada
		  	 
				FROM (
					 SELECT med_labprog."time",
						med_labprog.total AS consumo_total,
						med_labprog.iluminacao AS iluminacao,
						med_labprog.rede AS rede,
						med_labprog.ar_cond AS ar_cond,
						med_labprog.bancadas AS bancadas
					   FROM med_labprog
					  ORDER BY med_labprog."time"				
				) as filtro"""			  
		
    sqlFiltro=""
		  
    def getResultado(self,sql):
        conexao=ConexaoBD()
        resposta=conexao.consulta(sql)
        return(resposta)
		  

    def getAll(self):
        sql="""SELECT * FROM \"med_labprog\" """
        return(self.getResultado(sql))

    def getByInterval(self,dataInicio,dataFim):
        sqlSelect="""SELECT (extract(Day FROM subconsulta.hora)||'/'||extract(Month FROM subconsulta.hora)||'/'||extract(Year FROM subconsulta.hora)) as nData,
        sum(subconsulta.por_hora),
        """
        sqlFiltro="""WHERE  filtro."time" BETWEEN '"""+dataInicio+""" and '"""+dataFim+"""'
		 	            GROUP BY (time_bucket('01:00:00'::interval, filtro."time"))
		 	            ORDER BY (time_bucket('01:00:00'::interval, filtro."time")) DESC
		                 )as subconsulta		
		                 GROUP BY nData"""
        sql=sqlSelect + self.sqlBase +sqlFiltro 
    
    def getByDay(self,dia,mes,ano):
        sqlSelect="""SELECT (extract(Day FROM subconsulta.hora)||'/'||extract(Month FROM subconsulta.hora)||'/'||extract(Year FROM subconsulta.hora)) as nData,sum(subconsulta.por_hora)"""
        sqlFiltro="""WHERE extract(Day FROM filtro."time")="""+dia+""" extract(Month FROM filtro."time")="""+mes+""" and extract(Year FROM filtro."time")="""+ano+"""
		 	            GROUP BY (time_bucket('01:00:00'::interval, filtro."time"))
		 	            ORDER BY (time_bucket('01:00:00'::interval, filtro."time")) DESC
		                 )as subconsulta		
		                 GROUP BY nData"""
        sql=sqlSelect + self.sqlBase +sqlFiltro 

        return(self.getResultado(sql))
    def getByMonthDays(self,mes,ano):
        sqlSelect="""SELECT extract(Day FROM subconsulta.hora)as nData,sum(subconsulta.por_hora)"""
        sqlFiltro=""" WHERE extract(Month FROM filtro."time")="""+mes+""" and extract(Year FROM filtro."time")="""+ano+"""
		 	            GROUP BY (time_bucket('01:00:00'::interval, filtro."time"))
		 	            ORDER BY (time_bucket('01:00:00'::interval, filtro."time")) DESC
		                 )as subconsulta		
		                 GROUP BY nData"""
        sql=sqlSelect + self.sqlBase +sqlFiltro 

        return(self.getResultado(sql))


    def getByMonth(self,mes,ano):
        sqlSelect="""SELECT (extract(Month FROM subconsulta.hora)||'-'||extract(Year FROM subconsulta.hora)) as nData,sum(subconsulta.por_hora)"""
        sqlFiltro=""" WHERE extract(Month FROM filtro."time")="""+mes+""" and extract(Year FROM filtro."time")="""+ano+"""
		 	            GROUP BY (time_bucket('01:00:00'::interval, filtro."time"))
		 	            ORDER BY (time_bucket('01:00:00'::interval, filtro."time")) DESC
		                 )as subconsulta		
		                 GROUP BY nData"""
        sql=sqlSelect + self.sqlBase +sqlFiltro 

        return(self.getResultado(sql))

    def getByYearMonths(self,ano):
        sqlSelect="""SELECT extract(Month FROM subconsulta.hora) as nData,sum(subconsulta.por_hora) """
        sqlFiltro=""" WHERE extract(YEAR FROM filtro."time")="""+ ano +"""
		 	            GROUP BY (time_bucket('01:00:00'::interval, filtro."time"))
		 	            ORDER BY (time_bucket('01:00:00'::interval, filtro."time")) DESC
		                 )as subconsulta		
		                 GROUP BY nData"""
        sql=sqlSelect + self.sqlBase +sqlFiltro 

        return(self.getResultado(sql))

    def getByYear(self,ano):
        sqlSelect="""SELECT extract(YEAR FROM subconsulta.hora) as nData,sum(subconsulta.por_hora) """
        sqlFiltro=""" WHERE extract(YEAR FROM filtro."time")="""+ ano +"""
		 	            GROUP BY (time_bucket('01:00:00'::interval, filtro."time"))
		 	            ORDER BY (time_bucket('01:00:00'::interval, filtro."time")) DESC
		                 )as subconsulta		
		                 GROUP BY nData"""
        sql=sqlSelect + self.sqlBase +sqlFiltro 
        return(self.getResultado(sql))



#-----------------------------------------------------------------------------------------------------------------------


class MedLabSoft:
    sqlSelect=""
    
    sqlBase= """
        ,sum(subconsulta.iluminacao) as iluminacao,
        sum(subconsulta.rede) as rede,
        sum(subconsulta.ar) as ar,
        sum(subconsulta.bancada) as bancada,
        sum(subconsulta.servidor) as servidor
		FROM (SELECT time_bucket('01:00:00'::interval, filtro."time") AS hora,
				avg(filtro.consumo_total::numeric * 0.001) AS por_hora,	  
                avg(filtro.iluminacao::numeric * 0.001) AS iluminacao,
                avg(filtro.rede::numeric * 0.001) AS rede,
                avg(filtro.ar_cond::numeric * 0.001) AS ar,
                avg(filtro.bancadas::numeric * 0.001) AS bancada,
                avg(filtro.servidor::numeric * 0.001) AS servidor  
				FROM (
					 SELECT med_labsoft."time",
						med_labsoft.total AS consumo_total,
						med_labsoft.iluminacao AS iluminacao,
						med_labsoft.rede AS rede,
						med_labsoft.ar_cond AS ar_cond,
						med_labsoft.bancadas AS bancadas,
						med_labsoft.servidor AS servidor
					   FROM med_labsoft
					  ORDER BY med_labsoft."time"				
				) as filtro"""			  
		
    sqlFiltro=""
		  
    def getResultado(self,sql):
        conexao=ConexaoBD()
        resposta=conexao.consulta(sql)
        return(resposta)
		  

    def getAll(self):
        sql="""SELECT * FROM \"med_labsoft\" """
        return(self.getResultado(sql))

    def getByInterval(self,dataInicio,dataFim):
        sqlSelect="""SELECT (extract(Day FROM subconsulta.hora)||'/'||extract(Month FROM subconsulta.hora)||'/'||extract(Year FROM subconsulta.hora)) as nData,
        sum(subconsulta.por_hora),
        """
        sqlFiltro="""WHERE  filtro."time" BETWEEN '"""+dataInicio+""" and '"""+dataFim+"""'
		 	            GROUP BY (time_bucket('01:00:00'::interval, filtro."time"))
		 	            ORDER BY (time_bucket('01:00:00'::interval, filtro."time")) DESC
		                 )as subconsulta		
		                 GROUP BY nData"""
        sql=sqlSelect + self.sqlBase +sqlFiltro 
    
    def getByDay(self,dia,mes,ano):
        sqlSelect="""SELECT (extract(Day FROM subconsulta.hora)||'/'||extract(Month FROM subconsulta.hora)||'/'||extract(Year FROM subconsulta.hora)) as nData,sum(subconsulta.por_hora)"""
        sqlFiltro="""WHERE extract(Day FROM filtro."time")="""+dia+""" extract(Month FROM filtro."time")="""+mes+""" and extract(Year FROM filtro."time")="""+ano+"""
		 	            GROUP BY (time_bucket('01:00:00'::interval, filtro."time"))
		 	            ORDER BY (time_bucket('01:00:00'::interval, filtro."time")) DESC
		                 )as subconsulta		
		                 GROUP BY nData"""
        sql=sqlSelect + self.sqlBase +sqlFiltro 

        return(self.getResultado(sql))
    def getByMonthDays(self,mes,ano):
        sqlSelect="""SELECT extract(Day FROM subconsulta.hora)as nData,sum(subconsulta.por_hora)"""
        sqlFiltro=""" WHERE extract(Month FROM filtro."time")="""+mes+""" and extract(Year FROM filtro."time")="""+ano+"""
		 	            GROUP BY (time_bucket('01:00:00'::interval, filtro."time"))
		 	            ORDER BY (time_bucket('01:00:00'::interval, filtro."time")) DESC
		                 )as subconsulta		
		                 GROUP BY nData"""
        sql=sqlSelect + self.sqlBase +sqlFiltro 

        return(self.getResultado(sql))


    def getByMonth(self,mes,ano):
        sqlSelect="""SELECT (extract(Month FROM subconsulta.hora)||'-'||extract(Year FROM subconsulta.hora)) as nData,sum(subconsulta.por_hora)"""
        sqlFiltro=""" WHERE extract(Month FROM filtro."time")="""+mes+""" and extract(Year FROM filtro."time")="""+ano+"""
		 	            GROUP BY (time_bucket('01:00:00'::interval, filtro."time"))
		 	            ORDER BY (time_bucket('01:00:00'::interval, filtro."time")) DESC
		                 )as subconsulta		
		                 GROUP BY nData"""
        sql=sqlSelect + self.sqlBase +sqlFiltro 

        return(self.getResultado(sql))

    def getByYearMonths(self,ano):
        sqlSelect="""SELECT extract(Month FROM subconsulta.hora) as nData,sum(subconsulta.por_hora) """
        sqlFiltro=""" WHERE extract(YEAR FROM filtro."time")="""+ ano +"""
		 	            GROUP BY (time_bucket('01:00:00'::interval, filtro."time"))
		 	            ORDER BY (time_bucket('01:00:00'::interval, filtro."time")) DESC
		                 )as subconsulta		
		                 GROUP BY nData"""
        sql=sqlSelect + self.sqlBase +sqlFiltro 

        return(self.getResultado(sql))

    def getByYear(self,ano):
        sqlSelect="""SELECT extract(YEAR FROM subconsulta.hora) as nData,sum(subconsulta.por_hora) """
        sqlFiltro=""" WHERE extract(YEAR FROM filtro."time")="""+ ano +"""
		 	            GROUP BY (time_bucket('01:00:00'::interval, filtro."time"))
		 	            ORDER BY (time_bucket('01:00:00'::interval, filtro."time")) DESC
		                 )as subconsulta		
		                 GROUP BY nData"""
        sql=sqlSelect + self.sqlBase +sqlFiltro 
        return(self.getResultado(sql))

       

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

    

    def consumoMensal(self,mes=str(date.today().month),ano=str(date.today().year)):
        mediLabSoft=MedLabSoft()
        mediLabProg=MedLabProg()

        listaLabSoft=mediLabSoft.getByMonth(mes,ano)
        listaLabProg=mediLabProg.getByMonth(mes,ano)

        ls,lp=self.consumoAgrupado(listaLabSoft,listaLabProg)

        dados={ "mes":mes,
                "ano":ano,
                "labSoft": ls,
                "labProg":lp
        }

        # return(json.dumps(dados))
        return(dados)

    def consumoMensalDetalhado(self,mes=str(date.today().month),ano=str(date.today().year)):
        mediLabSoft=MedLabSoft()
        mediLabProg=MedLabProg()

        listaLabSoft=mediLabSoft.getByMonthDays(mes,ano)
        listaLabProg=mediLabProg.getByMonthDays(mes,ano)

        ls,lp=self.consumoDetalhado(listaLabSoft,listaLabProg,"dia")

        dados={ "mes":mes,
                "ano":ano,
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

        ls,lp=self.consumoAgrupado(listaLabSoft,listaLabProg)

        dados={ "ano":ano,
                "labSoft": ls,
                "labProg":lp
        }

        # return(json.dumps(dados))
        return(dados)

    def consumoAnualDetalhado(self,ano=str(date.today().year)):
        mediLabSoft=MedLabSoft()
        mediLabProg=MedLabProg()

        listaLabSoft=mediLabSoft.getByYearMonths(ano)
        listaLabProg=mediLabProg.getByYearMonths(ano)

        ls,lp=self.consumoDetalhado(listaLabSoft,listaLabProg,"mes")

        dados={ "ano":ano,
                "labSoft": ls,
                "labProg":lp
        }

        # return(json.dumps(dados))
        return(dados)




    def consumoDetalhado(self,listaS,listaP,vigencia):
        colunas=("Total","iluminacao","rede","ar_cond","bancadas","servidor")
        listaSoft= []

        for item in listaS:            
            listaDia=[]

            for c in range(1,len(colunas)+1):
                dado={}
                consumo=round(float(item[c]),2) 
                gasto=round(float(consumo)*0.4836,2)
                dado={  "nome": colunas[c-1],
                        "consumo":str(consumo),
                        "gasto": str(gasto)
                }
                listaDia.append(dado)
            listaSoft.append({
                vigencia: item[0],
                "dados":listaDia
            })


        listaProg=[]
        for item in listaP:            
            listaDia=[]

            for d in range(1,len(colunas)):
                dado={}
                consumo=round(float(item[d]),2) 
                gasto=round(float(consumo)*0.4836,2)
                dado={  "nome": colunas[d-1],
                        "consumo":str(consumo),
                        "gasto": str(gasto)
                }
                listaDia.append(dado)

            listaProg.append({
                vigencia: item[0],
                "dados":listaDia
            })

        return(listaSoft,listaProg)


    def consumoAgrupado(self,listaS,listaP):
        colunas=("Total","iluminacao","rede","ar_cond","bancadas","servidor")
        listaSoft= []

        for item in listaS:
            
            
            for a in range(1,len(colunas)+1):
                dado={}
                consumo=round(float(item[a]),2) 
                gasto=round(float(consumo)*0.4836,2)
                dado={  "nome": colunas[a-1],
                        "consumo":str(consumo),
                        "gasto": str(gasto)
                }
                listaSoft.append(dado)           


        i=0
        listaProg= []
        for item in listaP:
            dado={}
            for b in range(1,len(colunas)):
                consumo=round(float(item[b]),2) #kW
                gasto=round(float(consumo)*0.4836,2)
                dado={  "nome":colunas[b-1],
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
    # print(a.consumoAnual())
    # print(a.consumoMensal())
    # print(a.consumoMensalDetalhado())
    print(a.consumoAnualDetalhado())

    # tarifa: R$0,4836 o KWh

    # SELECT sum(total),sum(iluminacao),sum(servidor),sum(rede),sum(ar_cond),sum(bancadas) FROM med_labsoft WHERE time BETWEEN '2019-02-20' AND '2019-02-21' GROUP BY  DATE_PART('MONTH', time)

    # SELECT date_trunc('day', time)::date as nData,sum(total),sum(iluminacao),sum(servidor),sum(rede),sum(ar_cond),sum(bancadas) FROM med_labsoft WHERE time BETWEEN '2019-02-20' AND '2019-04-01' GROUP BY  date_trunc('day', time) ORDER BY nData; 

#      SELECT sum(subconsulta.por_hora) * 0.4288 AS total
#    FROM ( SELECT time_bucket('01:00:00'::interval, consumo_watts_labsoft."time") AS hora,
#             avg(consumo_watts_labsoft.consumo_total::numeric * 0.001) AS por_hora
#            FROM consumo_watts_labsoft
#           WHERE consumo_watts_labsoft."time" > (now() - '165 day'::interval)
#           GROUP BY (time_bucket('01:00:00'::interval, consumo_watts_labsoft."time"))
#           ORDER BY (time_bucket('01:00:00'::interval, consumo_watts_labsoft."time")) DESC) subconsulta;