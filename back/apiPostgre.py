#apiPostgre.py
import psycopg2

class ConexaoBD:

    def conectar(self,_host='143.107.102.7',database='medicoes',usuario='aluno',senha='labsoft'):
        self.conn = psycopg2.connect( host=_host,dbname=database,user=usuario, password=senha)
        self.cur = self.conn.cursor()

    def fecharConexao(self):
        self.cur.close()
        self.conn.close()

    def consulta(self,sql):        
        self.conectar()
        self.cur.execute(sql)
        resposta=self.cur.fetchall()
        self.fecharConexao() 
        return(resposta)

    def AddRemoveEdit(self,sql):
        self.conectar()
        self.cur.execute(sql)
        self.conn.commit()
        self.fecharConexao() 

# EXEMPLOS DE CRUD
# ("INSERT INTO \"nomeTabela\" (\"campo1\",\"campo2\") VALUES (%s, %s)",(valor1, valor2))
# ("SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE';")
# ("SELECT campo1,campo2... FROM nomeTabela WHERE condicional1 AND/OR condicional2...")

if (__name__=="__main__"):
    conect=ConexaoBD()
    sql="SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE';"
    sql="SELECT * FROM estacoes"
    resposta=conect.consulta(sql)
    for item in resposta:
        print(item)