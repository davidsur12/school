import sqlite3
from datetime import datetime


# Conectar a la base de datos (o crearla si no existe)

con = sqlite3.connect("school.db")
con.execute("PRAGMA foreign_keys = ON;")
# Crear un cursor para ejecutar consultas SQL
cursor = con.cursor()



def consultaCountries():
    cursor.execute("PRAGMA table_info(countries)")
    columnas = cursor.fetchall()
    for columna in columnas:
        
        if columna[0]:
            # El sexto elemento indica si es clave primaria (1) o no (0)
            print("Clave primaria:", columna[0])
    
    
    
def insertar_departamento( ):
    
    
    name = input('Ingresa el nombre del departamento')
    abrev = input('Ingresa el una abreviatura')
    descrip = input('Ingresa una descripcion')
    created_at, updated_at, deleted_at, id_country =datetime.now(), datetime.now(), None, 1
    
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
    name = str(input('Porafavor ingresa el nombre de la ciudad: '))
    abrev = str(input('Ingresa la abriviatura de la ciudad: '))
    descrip = str(input('ingresa una descripcion: '))
   
    cursor.execute("INSERT INTO countries ( name, abrev, descrip, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
                   (name, abrev, descrip , datetime.now(), datetime.now()))
    con.commit()
    print('Datos ingresados')

def cities():
    
    name = input('Ingresa el nombe')
    abrev = input('Ingresa la abreviatura')
    descrip = input('Ingresa la descricopn')
    id_dept, created_at, updated_at,= 1, datetime.now(), datetime.now()
    deleled_at=None
    cursor.execute("INSERT INTO cities (name, abrev, descrip, id_dept, created_at, updated_at, deleled_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
               (name, abrev, descrip, id_dept, created_at, updated_at, deleled_at))
    con.commit()
    
   
def insertar_persona():
    
    
    first_name = str(input('Ingresa el primer nombre (str): '))
    last_name = str(input('Ingresa el segundo nombre (str): '))
    id_ident_type = int(input('Ingresa el tipo de identidad (int): '))
    ident_number = str(input('Ingresa el numero de identidad (str): '))
    id_exp_city = int(input('Ingresa  la ciudad de exp (int): '))
    id_user = int(input('Ingresa  el id de usuario (int): '))
    address = str(input('Ingresa la direccion (str): '))
    mobile = str(input('Ingresa el numero de telefono (str): '))
    
    sql = '''INSERT INTO persons (first_name, last_name, id_ident_type, ident_number, id_exp_city, id_user, address, mobile, created_at, updated_at) 
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    # Datos a insertar
    datos = (first_name, last_name, id_ident_type, ident_number, id_exp_city, id_user, address, mobile, datetime.now(), datetime.now())
    # Ejecutar la consulta SQL
    cursor.execute(sql, datos)
    # Confirmar la transacción
    con.commit()
    print("Se ha insertado una nueva persona.")
 
 
def  insertar_users():
    email = input('Ingresa el email')
    password = input('Ingresa el password')
    status, created_at, updated_at = 1, datetime.now(), datetime.now()
    
    cursor.execute("INSERT INTO users (email, password, status, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
               (email, password, status, created_at, updated_at))  # El valor 1 representa True para el estado activo
    con.commit() 
    print('Datos ingresados') 
def insertar_students():
    
    
    code = input('Ingresa el codigo (str): ')
    id_person = int(input('Ingresa el id_person (int): '))
    status = int(input('ingresa el status (int): '))
    created_at = datetime.now()
    updated_at = datetime.now()
 
    
    cursor.execute("INSERT INTO students (code, id_person, status, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
               (code, id_person, status, created_at, updated_at))  # El valor 1 representa True para el estado activo
    con.commit()    
    print('Datos ingresados') 

 
def insertar_identificacon():
    id = int(input('Ingresa ID (int)'))
    name = str(input('Ingresa name (str)'))
    abrev = str(input('Ingresa la  abreviatura (str)'))
    descrip =  str(input('Ingresa la descripcion (str)'))
    
    created_at = datetime.now()
    updated_at = datetime.now()
    
    cursor.execute("INSERT INTO identification_types (id, name, abrev, descrip, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
               (id, name, abrev, descrip, created_at, updated_at))
    con.commit()   
    print('Datos ingresados') 
def menu():
    ciclo=True
    while ciclo:
     print('Ingresa las tablas en el siguiente orden por primera vez 7-6-5-1-3-2-4  ') 
     print('''
      
      Menu
[1]. Create user
[2]. Create student
[3]. Create identification type
[4]. Create person
[5]. Create cities
[6]. Create department
[7]. Create countries
[8]. Exit
      ''')
  
     
     opc = int(input('Seleciona una opcion: '))
    
    
     try:
         
         if(opc > 0 and opc< 9):
             
             print('Selecionaste la opcion' , str(opc))
             #consultaCountries()
             if(opc == 1):
              insertar_users()
             if(opc == 2):
              insertar_students()    
             if(opc == 3):
               insertar_identificacon()    
             if(opc == 4):
              insertar_persona()
        
             if(opc == 5):
              cities()
            
             if(opc == 7):
              countries()
              opc=0
             if(opc == 6):
            
              insertar_departamento()
              opc=0   
             if(opc == 8 ):
              print('saliste')
              ciclo=False
              break
       
        
            
         else:
             
             print('Opcion fuera de rango')    
             
     except Exception as e:
         print('Error al ingresar los datos')
                 
         
     
        
        
    
# 7-6-5-1-3-2-4   
menu()    
# Cerrar la conexión
con.close()
