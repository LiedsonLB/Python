from cassandra.cluster import Cluster

# Conectar ao banco de dados Cassandra
cluster = Cluster(['localhost'])
session = cluster.connect('nome_do_banco')

# Executar uma consulta simples
result = session.execute("SELECT * FROM tabela")

# Iterar sobre os resultados
for row in result:
    print(row)

# Fechar a conexão
session.shutdown()
cluster.shutdown()
