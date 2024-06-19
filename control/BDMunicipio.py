import re
from conecxion import Conexion

class BDMunicipio:
    def __init__(self):
        pass

    def obtenerDatos(self):
        objCon = Conexion()
        if not objCon.connection:
            return None, objCon.error_message
        sql = "SELECT * FROM Municipio WHERE activo = TRUE"
        resp = objCon.query_all(sql)
        objCon.close()
        return resp

    def guardar(self, nombre, id_entidad):
        if not self.validTxt(nombre):
            return False, "El nombre debe contener solo letras"
        if not self.validNum(id_entidad):
            return False, "El ID de la entidad debe ser un número"
        objCon = Conexion()
        if not objCon.connection:
            return False, objCon.error_message
        sql = f"INSERT INTO Municipio (nombre, id_entidad) VALUES ('{nombre}', {id_entidad})"
        success, error = objCon.exec_query(sql)
        objCon.close()
        return success, error

    def actualizar(self, id, nombre, id_entidad):
        if not self.validTxt(nombre):
            return False, "El nombre debe contener solo letras"
        if not self.validNum(id_entidad):
            return False, "El ID de la entidad debe ser un número"
        objCon = Conexion()
        if not objCon.connection:
            return False, objCon.error_message
        sql = f"UPDATE Municipio SET nombre = '{nombre}', id_entidad = {id_entidad} WHERE id_municipio = {id}"
        success, error = objCon.exec_query(sql)
        objCon.close()
        return success, error

    def borrar(self, id):
        objCon = Conexion()
        if not objCon.connection:
            return False, objCon.error_message
        sql = f"UPDATE Municipio SET activo = FALSE WHERE id_municipio = {id}"
        success, error = objCon.exec_query(sql)
        objCon.close()
        return success, error

    def validTxt(self, n):
        return all(char.isalpha() or char.isspace() for char in n)

    def validNum(self, n):
        return str(n).isdigit()
