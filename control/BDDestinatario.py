from conecxion import Conexion

class BDDestinatario:
    def __init__(self):
        pass

    def obtenerDatos(self):
        objCon = Conexion()
        if not objCon.connection:
            return None, objCon.error_message
        sql = "SELECT * FROM Destinatario WHERE activo = TRUE"
        resp = objCon.query_all(sql)
        objCon.close()
        return resp

    def guardar(self, nombre, direccion, id_municipio):
        objCon = Conexion()
        if not objCon.connection:
            return False, objCon.error_message
        sql = f"INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('{nombre}', '{direccion}', {id_municipio})"
        success, error = objCon.exec_query(sql)
        objCon.close()
        return success, error

    def actualizar(self, id, nombre, direccion, id_municipio):
        objCon = Conexion()
        if not objCon.connection:
            return False, objCon.error_message
        sql = f"UPDATE Destinatario SET nombre = '{nombre}', direccion = '{direccion}', id_municipio = {id_municipio} WHERE id_destinatario = {id}"
        success, error = objCon.exec_query(sql)
        objCon.close()
        return success, error

    def borrar(self, id):
        objCon = Conexion()
        if not objCon.connection:
            return False, objCon.error_message
        sql = f"UPDATE Destinatario SET activo = FALSE WHERE id_destinatario = {id}"
        success, error = objCon.exec_query(sql)
        objCon.close()
        return success, error
