import cx_Oracle

class OracleDB:

    def __init__(self, user, password, server, port, sid):
        self.tns = cx_Oracle.makedsn(server, port, sid)
        self.connection = None
        self.cursor = None
        self.user = user
        self.password = password
        self.sid = sid
        self.port = port
        self.server = server

    def connect(self):
        try:
            self.connection = cx_Oracle.connect(self.user, self.password, self.tns)
            self.cursor = self.connection.cursor()
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            if error.code == 1017:
                try:
                    self.user = 'C##'+self.user
                    self.connection = cx_Oracle.connect(self.user, self.password, self.tns)
                    self.cursor = self.connection.cursor()
                except cx_Oracle.DatabaseError as e:
                    print('{0} banco: {1}  servidor: {2}'.format(error.message,self.sid,self.server))
            else:
                print ('Erro de conexao com o banco de dados {0}: {1}'.format(self.sid,error.message) + '. Informar a equipe DBA.')

    def close(self):
        self.cursor.close()
        self.connection.close()

    def execute_sql_command(self, host, sid, query):
        self.connection = cx_Oracle.connect(self.user, self.password, self.tns)
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        
        return result