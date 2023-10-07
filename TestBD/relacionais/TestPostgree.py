import psycopg2

# Conectar ao banco de dados PostgreSQL
conn = psycopg2.connect(host='localhost', database='nome_do_banco', user='usuario', password='senha')

# Executar uma consulta simples
cursor = conn.cursor()
cursor.execute("SELECT * FROM tabela")
result = cursor.fetchall()

# Fechar a conexão
cursor.close()
conn.close()
