import mysql.connector

def conectar(consulta_sql):
    config = {
        'user': 'uzxqz8kn5gkz5jrl',
        'password': 'rMcwd3w8aVzkxkhA8Gu5',
        'host': 'biikh2v3gnklg76bq5xd-mysql.services.clever-cloud.com',
        'database': 'biikh2v3gnklg76bq5xd',
        'raise_on_warnings': True
    }

    try:
        conexion = mysql.connector.connect(**config)
        cursor = conexion.cursor()
        cursor.execute(consulta_sql)
        resultado = cursor.fetchall()
        conexion.close()
        return resultado
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None


