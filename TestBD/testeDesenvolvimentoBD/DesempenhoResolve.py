import time
import psycopg2  # Biblioteca para PostgreSQL
import mysql.connector  # Biblioteca para MySQL
import pymongo  # Biblioteca para MongoDB
import cx_Oracle  # Biblioteca para Oracle
import pyodbc  # Biblioteca para SQL Server
from neo4j import GraphDatabase  # Biblioteca para Neo4j
import redis  # Biblioteca para Redis
from cassandra.cluster import Cluster  # Biblioteca para Cassandra
import cockroachdb  # Biblioteca para CockroachDB
import pymysql  # Biblioteca para TiDB (MySQL)
import mariadb  # Biblioteca para MariaDB

# Configurações de conexão para cada banco de dados
postgres_config = {
    'host': 'localhost',
    'port': 5432,
    'database': 'mydatabase',
    'user': 'myuser',
    'password': 'mypassword'
}

mysql_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'Dream DB',
    'user': 'root',
    'password': ' '
}

mongodb_config = {
    'host': 'localhost',
    'port': 27017,
    'database': 'TestMongoDB',
    'user': '',
    'password': ''
}

oracle_config = {
    'user': 'myuser',
    'password': 'mypassword',
    'dsn': 'localhost:1521/mydatabase'
}

sqlserver_config = {
    'server': 'localhost',
    'database': 'mydatabase',
    'user': 'myuser',
    'password': 'mypassword'
}

neo4j_config = {
    'uri': 'bolt://localhost:7687',
    'user': 'myuser',
    'password': 'mypassword'
}

redis_config = {
    'host': 'localhost',
    'port': 6379,
    'password': 'mypassword'
}

cassandra_config = {
    'contact_points': ['localhost'],
    'port': 9042,
    'local_datacenter': 'datacenter1',
    'keyspace': 'mykeyspace',
    'username': 'myuser',
    'password': 'mypassword'
}

cockroachdb_config = {
    'host': 'localhost',
    'port': 26257,
    'database': 'mydatabase',
    'user': 'myuser',
    'password': 'mypassword'
}

tidb_config = {
    'host': 'localhost',
    'port': 4000,
    'database': 'mydatabase',
    'user': 'myuser',
    'password': 'mypassword'
}

mariadb_config = {
    'host': 'localhost',
    'port': 3306,
    'database': 'mydatabase',
    'user': 'myuser',
    'password': 'mypassword'
}

def measure_execution_time(operation):
    start_time = time.time()
    operation()
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

def postgres_insert():
    connection = psycopg2.connect(**postgres_config)
    cursor = connection.cursor()
    # Execute a operação de inserção no PostgreSQL
    cursor.execute("INSERT INTO mytable (nome) VALUES (%s)", (value1))
    connection.commit()
    cursor.close()
    connection.close()

def mysql_insert():
    connection = mysql.connector.connect(**mysql_config)
    cursor = connection.cursor()
    # Execute a operação de inserção no MySQL
    cursor.execute("INSERT INTO teste (nome) VALUES (%s)", ('Liedson',))
    connection.commit()
    cursor.close()
    connection.close()

def mongodb_insert():
    client = pymongo.MongoClient(**mongodb_config)
    db = client.TestMongoDB
    collection = db.TesteDeDB
    # Execute a operação de inserção no MongoDB
    document = {'nome': value1}
    collection.insert_one(document)
    client.close()

def oracle_insert():
    connection = cx_Oracle.connect(**oracle_config)
    cursor = connection.cursor()
    # Execute a operação de inserção no Oracle
    cursor.execute("INSERT INTO mytable (column1, column2) VALUES (:value1, :value2)", {'value1': value1, 'value2': value2})
    connection.commit()
    cursor.close()
    connection.close()

def sqlserver_insert():
    connection = pyodbc.connect(**sqlserver_config)
    cursor = connection.cursor()
    # Execute a operação de inserção no SQL Server
    cursor.execute("INSERT INTO mytable (column1, column2) VALUES (?, ?)", (value1, value2))
    connection.commit()
    cursor.close()
    connection.close()

def neo4j_insert():
    driver = GraphDatabase.driver(**neo4j_config)
    with driver.session() as session:
        # Execute a operação de inserção no Neo4j
        session.run("CREATE (n:Node {field1: $value1, field2: $value2})", value1=value1, value2=value2)

def redis_insert():
    r = redis.Redis(**redis_config)
    # Execute a operação de inserção no Redis
    r.set('key1', value1)
    r.set('key2', value2)

def cassandra_insert():
    cluster = Cluster(**cassandra_config)
    session = cluster.connect()
    # Execute a operação de inserção no Cassandra
    session.execute("INSERT INTO mytable (column1, column2) VALUES (?, ?)", (value1, value2))
    cluster.shutdown()

def cockroachdb_insert():
    connection = cockroachdb.connect(**cockroachdb_config)
    cursor = connection.cursor()
    # Execute a operação de inserção no CockroachDB
    cursor.execute("INSERT INTO mytable (column1, column2) VALUES (%s, %s)", (value1, value2))
    connection.commit()
    cursor.close()
    connection.close()

def tidb_insert():
    connection = pymysql.connect(**tidb_config)
    cursor = connection.cursor()
    # Execute a operação de inserção no TiDB
    cursor.execute("INSERT INTO mytable (column1, column2) VALUES (%s, %s)", (value1, value2))
    connection.commit()
    cursor.close()
    connection.close()

def mariadb_insert():
    connection = mariadb.connect(**mariadb_config)
    cursor = connection.cursor()
    # Execute a operação de inserção no MariaDB
    cursor.execute("INSERT INTO mytable (column1, column2) VALUES (%s, %s)", (value1, value2))
    connection.commit()
    cursor.close()
    connection.close()

# Valores de exemplo para inserção
value1 = "Liedson"
value2 = "Value 2"

# Medição do tempo de inserção
postgres_insert_time = measure_execution_time(postgres_insert)
mysql_insert_time = measure_execution_time(mysql_insert)
mongodb_insert_time = measure_execution_time(mongodb_insert)
oracle_insert_time = measure_execution_time(oracle_insert)
sqlserver_insert_time = measure_execution_time(sqlserver_insert)
neo4j_insert_time = measure_execution_time(neo4j_insert)
redis_insert_time = measure_execution_time(redis_insert)
cassandra_insert_time = measure_execution_time(cassandra_insert)
cockroachdb_insert_time = measure_execution_time(cockroachdb_insert)
tidb_insert_time = measure_execution_time(tidb_insert)
mariadb_insert_time = measure_execution_time(mariadb_insert)

# Realize a medição para outras operações (consulta, atualização, etc.)

# Exemplo de saída dos tempos de execução
print("Tempo de inserção no PostgreSQL:", postgres_insert_time)
print("Tempo de inserção no MySQL:", mysql_insert_time)
print("Tempo de inserção no MongoDB:", mongodb_insert_time)
print("Tempo de inserção no Oracle:", oracle_insert_time)
print("Tempo de inserção no SQL Server:", sqlserver_insert_time)
print("Tempo de inserção no Neo4j:", neo4j_insert_time)
print("Tempo de inserção no Redis:", redis_insert_time)
print("Tempo de inserção no Cassandra:", cassandra_insert_time)
print("Tempo de inserção no CockroachDB:", cockroachdb_insert_time)
print("Tempo de inserção no TiDB:", tidb_insert_time)
print("Tempo de inserção no MariaDB:", mariadb_insert_time)

# Compare os resultados e determine qual banco de dados apresenta o melhor desempenho