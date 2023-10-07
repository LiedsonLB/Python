import cx_Oracle

# Conectar ao banco de dados Oracle
conn = cx_Oracle.connect('usuario/senha@localhost:1521/nome_do_banco')

# Executar uma consulta simples
cursor = conn.cursor()
cursor.execute("SELECT * FROM tabela")
result = cursor.fetchall()

# Fechar a conexão
cursor.close()
conn.close()
