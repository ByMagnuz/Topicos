import re
from conecxion import Conexion

class BDDestinatario:
    def __init__(self):
        pass

    def obtenerDatos(self):
        objCon = Conexion()
        
        # Verificar la conexión
        if not objCon.connection:
            return None, objCon.error_message
        
        sql = "SELECT * FROM destinatario WHERE activo = TRUE"
        
        try:
            # Ejecutar la consulta SQL
            resp = objCon.query_all(sql)
            
            # Verificar la respuesta
            if not resp:
                return None, "No se encontraron registros."
            
            # Obtener nombres de columnas y datos
            columns = [desc[0] for desc in objCon.description]
            data = resp
            
            # Cerrar la conexión
            objCon.close()
            
            return (columns, data), None
        except Exception as e:
            objCon.close()
            return None, str(e)

    def guardar(self, nombre, direccion, id_municipio):
        if not self.validTxt(nombre):
            return False, "El nombre debe contener solo letras"
        if not self.validTxt(direccion):
            return False, "La dirección debe contener solo letras y números"
        if not self.validNum(id_municipio):
            return False, "El ID del municipio debe ser un número"
        objCon = Conexion()
        if not objCon.connection:
            return False, objCon.error_message
        sql = f"INSERT INTO Destinatario (nombre, direccion, id_municipio) VALUES ('{nombre}', '{direccion}', {id_municipio})"
        success, error = objCon.exec_query(sql)
        objCon.close()
        return success, error

    def actualizar(self, id, nombre, direccion, id_municipio):
        if not self.validTxt(nombre):
            return False, "El nombre debe contener solo letras"
        if not self.validTxt(direccion):
            return False, "La dirección debe contener solo letras y números"
        if not self.validNum(id_municipio):
            return False, "El ID del municipio debe ser un número"
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

    def validTxt(self, n):
        return all(char.isalnum() or char.isspace() for char in n)

    def validNum(self, n):
        return str(n).isdigit()
