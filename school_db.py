import sqlite3

import os

# Especifica la ruta del archivo de la base de datos
ruta_base_de_datos = 'school.db'
if os.path.exists(ruta_base_de_datos):
    # Elimina el archivo de la base de datos
    os.remove(ruta_base_de_datos)
    print("La base de datos ha sido eliminada exitosamente.")
else:
    print("La base de datos no existe.")
    
con = sqlite3.connect("school.db")
con.execute("PRAGMA foreign_keys = ON")
cursor = con.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS countries (
                    id INTEGER PRIMARY KEY NOT NULL ,
                    name VARCHAR(100) NOT NULL,
                    abrev VARCHAR(10) NOT NULL,
                    descrip VARCHAR(10) NOT NULL,
                    created_at DATETIME NOT NULL,
                    updated_at DATETIME NOT NULL,
                    deleled_at DATETIME NULL
                    
                    )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS departments (
                   
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    abrev VARCHAR(10) NOT NULL,
                    descrip VARCHAR(10) NOT NULL,
                    created_at  DATETIME  NOT NULL,
                    updated_at  DATETIME  NOT NULL,
                    deleled_at  DATETIME  NULL,
                    id_country INTEGER NOT NULL,
                    FOREIGN KEY  (id_country)   REFERENCES countries(id)
                    
                    )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS cities (
                   
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    abrev VARCHAR(10) NOT NULL,
                    descrip VARCHAR(10) NOT NULL,
                    id_dept INTEGER,
                    created_at DATETIME NOT NULL,
                    updated_at DATETIME NOT NULL,
                    deleled_at DATETIME NULL,
                    FOREIGN KEY (id_dept) REFERENCES departments(id)
                    
                    )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS persons (
                   
                    id INTEGER PRIMARY KEY,
                    first_name VARCHAR(50) NOT NULL,
                    last_name VARCHAR(10) NOT NULL,
                    id_ident_type INTEGER NOT NULL,
                    ident_number VARCHAR(15) NOT NULL,
                    id_exp_city INTEGER,
                    id_user INTEGER,
                    address VARCHAR(50) NOT NULL,
                    mobile VARCHAR(50) NOT NULL,
                    created_at DATETIME NOT NULL,
                    updated_at DATETIME NOT NULL,
                    deleled_at DATETIME NULL,
                        FOREIGN KEY (id_exp_city) REFERENCES cities(id),
                        FOREIGN KEY (id_user) REFERENCES users(id)
                    
                    )''')


cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY,
                   email VARCHAR(50) NOT NULL,
                   password VARCHAR(250) NOT NULL,
                   status BOOLEAN NULL,
                   created_at DATETIME NOT NULL,
                   updated_at DATETIME NOT NULL,
                   deleled_at DATETIME NULL
                    
                    )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS identification_types (
                   id INTEGER  PRIMARY KEY,
                   name VARCHAR(50) NOT NULL,
                    abrev VARCHAR(10) NOT NULL,
                    descrip VARCHAR(100) NOT NULL,
                    created_at DATETIME NOT NULL,
                    updated_at DATETIME NOT NULL,
                    deleled_at DATETIME NULL,
                    FOREIGN KEY (id) REFERENCES persons(id_ident_type)
                    
                    )''')


cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                   id INTEGER PRIMARY KEY,
                   code VARCHAR(50) NOT NULL,
                   id_person INTEGER ,
                   status BOOLEAN NULL,
                    created_at DATETIME NOT NULL,
                    updated_at DATETIME NOT NULL,
                    deleled_at DATETIME NULL,
                      FOREIGN KEY (id_person) REFERENCES persons(id)
                    
                    )''')

con.commit()
con.close()


