from conecxion import Conexion

class BDMunicipio:
    def __init__(self):
        pass

    def obtenerDatos(self):
        objCon = Conexion()
        r = objCon.conexionMariaDB()
        if r is not None:
            sql = "SELECT * FROM Municipio WHERE activo = 1"
            resp = objCon.query_all(r, sql)
            r.close()
            return resp
        return False

    def borrarLogico(self, id):
        objCon = Conexion()
        r = objCon.conexionMariaDB()
        if r is not None:
            sql = f"UPDATE Municipio SET activo = 0 WHERE id_municipio = {id}"
            resp = objCon.exec_query(r, sql)
            r.close()
            return resp
        return False

    def guardar(self, nombre, id_entidad):
        objCon = Conexion()
        c = objCon.conexionMariaDB()
        if c is not None:
            sql = f"SELECT id_municipio FROM Municipio WHERE nombre = '{nombre}' AND id_entidad = {id_entidad};"
            existe = objCon.exist(c, sql)
            if not existe:
                sql = "SELECT max(id_municipio) FROM Municipio;"
                n = objCon.getNextID(c, sql)
                sql = f"INSERT INTO Municipio VALUES({n}, '{nombre}', {id_entidad}, 1);"
                ok = objCon.exec_query(c, sql)
                c.close()
                return ok
            return False
