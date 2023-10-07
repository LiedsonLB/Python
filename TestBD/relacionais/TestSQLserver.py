import pyodbc

# Conectar ao banco de dados SQL Server
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=nome_do_banco;UID=usuario;PWD=senha')

# Executar uma consulta simples
cursor = conn.cursor()
cursor.execute("SELECT * FROM tabela")
result = cursor.fetchall()

# Fechar a conexão
cursor.close()
conn.close()
