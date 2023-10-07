from py2neo import Graph

# Conectar ao banco de dados Neo4j
graph = Graph("bolt://localhost:7687", auth=("usuario", "senha"))

# Executar uma consulta Cypher simples
result = graph.run("MATCH (n) RETURN n")

# Iterar sobre os resultados
for record in result:
    print(record)

# Fechar a conexão
graph.close()
