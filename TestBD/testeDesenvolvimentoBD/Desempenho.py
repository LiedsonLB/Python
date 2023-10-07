import time
import psycopg2
import mysql.connector
import pymongo
import cx_Oracle
import pyodbc
from neo4j import GraphDatabase
import redis
from cassandra.cluster import Cluster
import cockroachdb
import pymysql
import mariadb

# Configurações de conexão para cada banco de dados

# Configuração do PostgreSQL
postgres_config = {
    'host': 'localhost',
    'port': 5432,
    'database': 'TestePost',
    'user': 'postgres',
    'password': '141063'
}

# Configuração do MySQL
mysql_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'experimentodb',
    'user': 'root',
    'password': ''
}

# Configuração do MongoDB
mongodb_config = {
    'host': 'localhost',
    'port': 27017,
    'database': 'mydatabase',
    'user': 'myuser',
    'password': 'mypassword'
}

# Configuração do Oracle
oracle_config = {
    'user': 'myuser',
    'password': 'mypassword',
    'dsn': 'localhost:1521/mydatabase'
}

# Configuração do SQL Server
sqlserver_config = {
    'server': 'localhost',
    'database': 'mydatabase',
    'user': 'myuser',
    'password': 'mypassword'
}

# Configuração do Neo4j
neo4j_config = {
    'uri': 'bolt://localhost:7687',
    'user': 'myuser',
    'password': 'mypassword'
}

# Configuração do Redis
redis_config = {
    'host': 'localhost',
    'port': 6379,
    'password': 'mypassword'
}

# Configuração do Cassandra
cassandra_config = {
    'contact_points': ['localhost'],
    'port': 9042,
    'local_datacenter': 'datacenter1',
    'keyspace': 'mykeyspace',
    'username': 'myuser',
    'password': 'mypassword'
}

# Configuração do CockroachDB
cockroachdb_config = {
    'host': 'localhost',
    'port': 26257,
    'database': 'mydatabase',
    'user': 'myuser',
    'password': 'mypassword'
}

# Configuração do TiDB (MySQL)
tidb_config = {
    'host': 'localhost',
    'port': 4000,
    'database': 'mydatabase',
    'user': 'myuser',
    'password': 'mypassword'
}

# Configuração do MariaDB
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
    cursor.execute("INSERT INTO users (nome) VALUES (%s)", (value,))
    connection.commit()
    cursor.close()
    connection.close()

def mysql_insert():
    connection = mysql.connector.connect(**mysql_config)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO teste (nome) VALUES (%s)", (value,))
    connection.commit()
    cursor.close()
    connection.close()

def mongodb_insert():
    client = pymongo.MongoClient(**mongodb_config)
    db = client.mydatabase
    collection = db.mycollection
    document = {'field1': value, 'field2': value}
    collection.insert_one(document)
    client.close()

def oracle_insert():
    connection = cx_Oracle.connect(**oracle_config)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO mytable (column1, column2) VALUES (:value, :value)", {'value': value})
    connection.commit()
    cursor.close()
    connection.close()

def sqlserver_insert():
    connection = pyodbc.connect(**sqlserver_config)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO mytable (column1, column2) VALUES (?, ?)", (value, value))
    connection.commit()
    cursor.close()
    connection.close()

def neo4j_insert():
    driver = GraphDatabase.driver(**neo4j_config)
    with driver.session() as session:
        session.run("CREATE (n:Node {field1: $value, field2: $value})", value=value)

def redis_insert():
    r = redis.Redis(**redis_config)
    r.set('key', value)

def cassandra_insert():
    cluster = Cluster(**cassandra_config)
    session = cluster.connect()
    session.execute("INSERT INTO mytable (column1, column2) VALUES (?, ?)", (value, value))
    cluster.shutdown()

def cockroachdb_insert():
    connection = cockroachdb.connect(**cockroachdb_config)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO mytable (column1, column2) VALUES (%s, %s)", (value, value))
    connection.commit()
    cursor.close()
    connection.close()

def tidb_insert():
    connection = pymysql.connect(**tidb_config)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO mytable (column1, column2) VALUES (%s, %s)", (value, value))
    connection.commit()
    cursor.close()
    connection.close()

def mariadb_insert():
    connection = mariadb.connect(**mariadb_config)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO mytable (column1, column2) VALUES (%s, %s)", (value, value))
    connection.commit()
    cursor.close()
    connection.close()

def add_data_to_databases(value, num_times):
    print("Inserindo dados em todos os bancos...")
    print()

    # Medição do tempo de inserção para cada banco de dados
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

    # Imprime os tempos de inserção para cada banco de dados
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

# Valores de exemplo para inserção
value = "Liedson"

# Número de vezes que o dado será adicionado
num_times = 10

# Chamada da função para adicionar dados aos bancos de dados
add_data_to_databases(value, num_times)