from conecxion import Conexion

class BDDestinatario:
    def __init__(self):
        pass

    def obtenerDatos(self):
        objCon = Conexion()
        if not objCon.connection:
            return None, objCon.error_message
        sql = "SELECT id_destinatario, nombre, direccion, id_municipio FROM Destinatario WHERE activo = TRUE"
        resp = objCon.query_all(sql)
        objCon.close()
        if resp:
            columns = ["ID", "Nombre", "Dirección", "ID Municipio"]
            print("Datos obtenidos de la base de datos:", resp)  # Añadir impresión de depuración
            return (columns, resp), None
        return None, "No se encontraron datos"

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
