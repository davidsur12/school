import sqlite3
from datetime import datetime

# Conectar a la base de datos (o crearla si no existe)

con = sqlite3.connect("school.db")
con.execute("PRAGMA foreign_keys = ON;")
# Crear un cursor para ejecutar consultas SQL
cursor = con.cursor()

# Definir una función para insertar datos en la tabla departments
def insertar_departamento(name, abrev, descrip, created_at, updated_at, deleted_at, id_country):
    # Sentencia SQL para insertar un nuevo registro en la tabla departments
    sql = '''INSERT INTO departments (name, abrev, descrip, created_at, updated_at, deleled_at, id_country) 
             VALUES (?, ?, ?, ?, ?, ?, ?)'''
    # Datos a insertar
    datos = (name, abrev, descrip, created_at, updated_at, deleted_at, id_country)
    # Ejecutar la consulta SQL
    cursor.execute(sql, datos)
    # Confirmar la transacción
    con.commit()
    print("Se ha insertado un nuevo departamento.")
  

def countries():
    cursor.execute("INSERT INTO countries ( name, abrev, descrip, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
               ("País 1", "PA", "Descripción país 1", datetime.now(), datetime.now()))
    con.commit()


def cities(name, abrev, descrip, id_dept, created_at, updated_at, deleled_at):
    cursor.execute("INSERT INTO cities (name, abrev, descrip, id_dept, created_at, updated_at, deleled_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
               (name, abrev, descrip, id_dept, created_at, updated_at, deleled_at))
    con.commit()
    
   
def insertar_persona(first_name, last_name, id_ident_type, ident_number, id_exp_city, id_user, address, mobile):
    # Sentencia SQL para insertar un nuevo registro en la tabla persons
    sql = '''INSERT INTO persons (first_name, last_name, id_ident_type, ident_number, id_exp_city, id_user, address, mobile, created_at, updated_at) 
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    # Datos a insertar
    datos = (first_name, last_name, id_ident_type, ident_number, id_exp_city, id_user, address, mobile, datetime.now(), datetime.now())
    # Ejecutar la consulta SQL
    cursor.execute(sql, datos)
    # Confirmar la transacción
    con.commit()
    print("Se ha insertado una nueva persona.")
 
 
def  insertar_users(email, password, status, created_at, updated_at):
    cursor.execute("INSERT INTO users (email, password, status, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
               (email, password, status, created_at, updated_at))  # El valor 1 representa True para el estado activo
    con.commit() 
    
def insertar_students(code, id_person, status, created_at, updated_at):
    cursor.execute("INSERT INTO students (code, id_person, status, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
               (code, id_person, status, created_at, updated_at))  # El valor 1 representa True para el estado activo
    con.commit()    
 

 
def insertar_identificacon(id, name, abrev, descrip, created_at, updated_at):
    cursor.execute("INSERT INTO identification_types (id, name, abrev, descrip, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
               (id, name, abrev, descrip, created_at, updated_at))
    con.commit()    
def menu():
    ciclo=True
    while ciclo:
        
     print('''
      
      Menú
[1]. Create user
[2]. Create student
[3]. Create identification type
[4]. Create person
[5]. Create cities
[6]. Create department
[7]. Create countries
[8]. Exit
      ''')
     opc = int(input())
    
    
    
     if(opc > 0 and opc< 9):
        print('Selecionaste la opcion' , str(opc))
        if(opc == 1):
            insertar_users("usuario@example.com", "contraseña", 1, datetime.now(), datetime.now())
        if(opc == 2):
            insertar_students("Código", 1, 1, datetime.now(), datetime.now())    
        if(opc == 3):
             insertar_identificacon(1, "Tipo de identificación 1", "TI1", "Descripción del tipo de identificación 1", datetime.now(), datetime.now())    
        if(opc == 4):
            insertar_persona("Nombre", "Apellido", 1, "123456789", 1,1, "Dirección", "123456789")
        
        if(opc == 5):
            cities("Ciudad 1", "C1", "Descripción ciudad 1", 1, datetime.now(), datetime.now(), None)
            
        if(opc == 7):
            countries()
            opc=0
        if(opc == 6):
            insertar_departamento("Departamento 1", "Dep1", "Descripción 1", datetime.now(), datetime.now(), None, 1)
            opc=0   
        if(opc == 8 ):
            print('saliste')
            ciclo=False
            break
            
     else:
        print('Opcion fuera de rango')    
        
        
    
    
menu()    
# Cerrar la conexión
con.close()
