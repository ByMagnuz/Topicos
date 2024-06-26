from conecxion import Conexion

class BDEntidadFederativa:
    def __init__(self):
        pass

    def obtenerDatos(self):
        objCon = Conexion()
        r = objCon.conexionMariaDB()
        if r is not None:
            sql = "SELECT * FROM Entidad_Federativa WHERE activo = 1"
            resp = objCon.query_all(r, sql)
            r.close()
            return resp
        return False

    def obtenerDatosPorID(self, id):
        objCon = Conexion()
        r = objCon.conexionMariaDB()
        if r is not None:
            sql = f"SELECT * FROM Entidad_Federativa WHERE id_entidad = {id}"
            resp = objCon.query_all(r, sql)
            r.close()
            if resp and resp[1]:
                return dict(zip(resp[0], resp[1][0]))
        return None

    def borrarLogico(self, id):
        objCon = Conexion()
        r = objCon.conexionMariaDB()
        if r is not None:
            sql = f"UPDATE Entidad_Federativa SET activo = 0 WHERE id_entidad = {id}"
            resp = objCon.exec_query(r, sql)
            r.close()
            if resp:
                return "Registro borrado correctamente."
        return "Error al borrar el registro."

    def guardar(self, nombre):
        objCon = Conexion()
        c = objCon.conexionMariaDB()
        if c is not None:
            sql = f"SELECT id_entidad FROM Entidad_Federativa WHERE nombre = '{nombre}';"
            existe = objCon.exist(c, sql)
            if not existe:
                sql = "SELECT max(id_entidad) FROM Entidad_Federativa;"
                n = objCon.getNextID(c, sql)
                sql = f"INSERT INTO Entidad_Federativa VALUES({n}, '{nombre}', 1);"
                ok = objCon.exec_query(c, sql)
                c.close()
                if ok:
                    return "Registro insertado correctamente."
            return "El registro ya existe."
        return "Error al insertar el registro."
    
    def actualizar(self, id_entidad, nombre):
        objCon = Conexion()
        c = objCon.conexionMariaDB()
        if c is not None:
            sql = f"UPDATE Entidad_Federativa SET nombre='{nombre}' WHERE id_entidad={id_entidad}"
            ok = objCon.exec_query(c, sql)
            c.close()
            if ok:
                return "Registro actualizado correctamente."
        return "Error al actualizar el registro."
