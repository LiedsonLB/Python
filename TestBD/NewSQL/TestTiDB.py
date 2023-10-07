import pymysql

# Conectar ao banco de dados TiDB
conn = pymysql.connect(
    host="localhost",
    port=4000,
    user="root",
    password="",
    database="your_database"
)

# Criar um cursor
cursor = conn.cursor()

# Executar uma consulta
cursor.execute("SELECT * FROM your_table")

# Obter os resultados
results = cursor.fetchall()

# Imprimir os resultados
for row in results:
    print(row)

# Fechar o cursor e a conexão
cursor.close()
conn.close()
