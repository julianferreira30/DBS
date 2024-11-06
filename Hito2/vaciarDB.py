import psycopg2

conn = psycopg2.connect(
    host="cc3201.dcc.uchile.cl",
    database="cc3201",
    user="cc3201",
    password="cc3201",
    port="5508"
)

cur = conn.cursor()

# Lista de todas las tablas que deseas vaciar
tables = [
    "medalla", 
    "evento_atleta", 
    "atleta_pais", 
    "entrenador_atleta", 
    "evento_disciplina", 
    "disciplina", 
    "evento", 
    "pais", 
    "entrenador", 
    "atleta"
]

# Vaciar todas las tablas
for table in tables:
    cur.execute(f"TRUNCATE TABLE {table} RESTART IDENTITY CASCADE")

# Confirmar cambios
conn.commit()

print("Todas las tablas han sido vaciadas.")

# Cerrar conexión
cur.close()
conn.close()
