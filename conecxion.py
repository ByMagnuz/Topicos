import pyodbc

class Conexion(object):
    def __init__(self):
        pass

    def conexionMariaDB(self):
        try:
            txt = "DRIVER={MariaDB ODBC 3.1 Driver}; SERVER=localhost; UID=root; PWD=; DATABASE=ProyectoTop; PORT=3306"
            conn = pyodbc.connect(txt)
        except Exception as err:
            conn = None
        return conn
    
    def query_all(self, con, sql):
        cur = con.cursor()
        cur.execute(sql)
        r = cur.fetchall()
        nom = [column[0] for column in cur.description]
        resp = [nom, r]
        cur.close()
        return resp
    
    def exec_query(self, con, sql):
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        cur.close()
        return True
    
    def exist(self, c, sql):
        cur = c.cursor()
        cur.execute(sql)
        r = cur.fetchone()
        cur.close()
        return r is not None
        
    def getNextID(self, c, sql):
        cur = c.cursor()
        cur.execute(sql)
        r = cur.fetchone()
        n = r[0] + 1
        cur.close()
        return n
