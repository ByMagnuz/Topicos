import pyodbc

class Conexion:
    def __init__(self):
        try:
            self.connection = pyodbc.connect(
                "DRIVER={MariaDB ODBC 3.1 Driver}; SERVER=localhost; UID=root; PWD=; DATABASE=ProyectoTop; PORT=3306"
            )
        except pyodbc.Error as e:
            self.connection = None
            self.error_message = str(e)

    def query_all(self, sql):
        if not self.connection:
            return None, self.error_message
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
        return columns, result

    def exec_query(self, sql):
        if not self.connection:
            return False, self.error_message
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            self.connection.commit()
        return True, None

    def close(self):
        if self.connection:
            self.connection.close()
