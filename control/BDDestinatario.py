from conecxion import Conexion

class BDDestinatario:
    def __init__(self):
        pass

    def obtenerDatos(self):
        objCon = Conexion()
        r = objCon.conexionMariaDB()
        if r is not None:
            sql = "SELECT * FROM Destinatario WHERE activo = 1"
            resp = objCon.query_all(r, sql)
            r.close()
            return resp
        return False

    def obtenerDatosPorID(self, id):
        objCon = Conexion()
        r = objCon.conexionMariaDB()
        if r is not None:
            sql = f"SELECT * FROM Destinatario WHERE id_destinatario = {id}"
            resp = objCon.query_all(r, sql)
            r.close()
            if resp and resp[1]:
                return dict(zip(resp[0], resp[1][0]))
        return None

    def borrarLogico(self, id):
        objCon = Conexion()
        r = objCon.conexionMariaDB()
        if r is not None:
            sql = f"UPDATE Destinatario SET activo = 0 WHERE id_destinatario = {id}"
            resp = objCon.exec_query(r, sql)
            r.close()
            if resp:
                return "Registro borrado correctamente."
        return "Error al borrar el registro."

    def guardar(self, nombre, direccion, id_municipio):
        objCon = Conexion()
        c = objCon.conexionMariaDB()
        if c is not None:
            sql = f"SELECT id_destinatario FROM Destinatario WHERE nombre = '{nombre}' AND direccion = '{direccion}';"
            existe = objCon.exist(c, sql)
            if not existe:
                sql = "SELECT max(id_destinatario) FROM Destinatario;"
                n = objCon.getNextID(c, sql)
                sql = f"INSERT INTO Destinatario VALUES({n}, '{nombre}', '{direccion}', {id_municipio}, 1);"
                ok = objCon.exec_query(c, sql)
                c.close()
                if ok:
                    return "Registro insertado correctamente."
            return "El registro ya existe."
        return "Error al insertar el registro."
    
    def actualizar(self, id_destinatario, nombre, direccion, id_municipio):
        objCon = Conexion()
        c = objCon.conexionMariaDB()
        if c is not None:
            sql = f"UPDATE Destinatario SET nombre='{nombre}', direccion='{direccion}', id_municipio={id_municipio} WHERE id_destinatario={id_destinatario}"
            ok = objCon.exec_query(c, sql)
            c.close()
            if ok:
                return "Registro actualizado correctamente."
        return "Error al actualizar el registro."
