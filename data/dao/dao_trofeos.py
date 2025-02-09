from data.modelo.trofeo import Trofeo

class DaoTrofeos:
    
    def get_all(self,db) -> list[Trofeo]:
        cursor = db.cursor()
    
        cursor.execute("SELECT * FROM trofeos")

        equipos_en_db = cursor.fetchall()
        equipos : list[Trofeo]= list()
        for equipo in equipos_en_db:
            alumno = Trofeo(equipo[0], equipo[1])
            equipos.append(alumno)
        cursor.close()
        
        return equipos
    
    def insert(self, db, nombre: str):
        cursor = db.cursor()
        sql = ("INSERT INTO trofeos (nombre) values (%s) ")
        data = (nombre,)
        cursor.execute(sql,data)
        # cursor.execute(f"INSERT INTO trofeos (nombre) VALUES ('{nombre}')")
        db.commit()
        cursor.close()

    def delete(self, db, id: str):
        cursor = db.cursor()
        sql = ("DELETE FROM  trofeos where id = (%s) ")
        data = (id,)
        cursor.execute(sql,data)
        # cursor.execute(f"DELETE INTO trofeos (nombre) VALUES ('{nombre}')")
        db.commit()
        cursor.close()
    
    def update(self, db, id: int, nombre: str):
        cursor = db.cursor()
        sql = "UPDATE trofeos SET nombre = %s WHERE id = %s"
        cursor.execute(sql, (nombre, id))
        db.commit()
        cursor.close()