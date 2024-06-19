import re
from conecxion import Conexion

class BDEntidadFederativa:
    def __init__(self):
        pass

    def obtenerDatos(self):
        objCon = Conexion()
        if not objCon.connection:
            return None, objCon.error_message
        sql = "SELECT * FROM Entidad_Federativa WHERE activo = TRUE"
        resp = objCon.query_all(sql)
        objCon.close()
        return resp

    def guardar(self, nombre):
        if not self.validTxt(nombre):
            return False, "El nombre debe contener solo letras"
        objCon = Conexion()
        if not objCon.connection:
            return False, objCon.error_message
        sql = f"INSERT INTO Entidad_Federativa (nombre) VALUES ('{nombre}')"
        success, error = objCon.exec_query(sql)
        objCon.close()
        return success, error

    def actualizar(self, id, nombre):
        if not self.validTxt(nombre):
            return False, "El nombre debe contener solo letras"
        objCon = Conexion()
        if not objCon.connection:
            return False, objCon.error_message
        sql = f"UPDATE Entidad_Federativa SET nombre = '{nombre}' WHERE id_entidad = {id}"
        success, error = objCon.exec_query(sql)
        objCon.close()
        return success, error

    def borrar(self, id):
        objCon = Conexion()
        if not objCon.connection:
            return False, objCon.error_message
        sql = f"UPDATE Entidad_Federativa SET activo = FALSE WHERE id_entidad = {id}"
        success, error = objCon.exec_query(sql)
        objCon.close()
        return success, error

    def validTxt(self, n):
        return all(char.isalpha() or char.isspace() for char in n)
