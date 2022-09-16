import MySQLdb

DB_HOST = 'database-pi-1.ccnz3ucpvxy8.us-east-1.rds.amazonaws.com' 
DB_USER = 'admin' 
DB_PASS = 'cXeU5U5aEwTiwZYYH4QL' 
DB_NAME = 'pi-01' 

def run_query(query = ''): 

    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
    conn = MySQLdb.connect(*datos)                  # Conectar a la base de datos 
    cursor = conn.cursor()                          # Crear un cursor 
    cursor.execute(query)                           # Ejecutar una consulta 

    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()                    # Traer los resultados de un select 
    else: 
        conn.commit()                               # Hacer efectiva la escritura de datos 
        data = None 
    
    cursor.close()                                  # Cerrar el cursor 
    conn.close()                                    # Cerrar la conexión 

    return data