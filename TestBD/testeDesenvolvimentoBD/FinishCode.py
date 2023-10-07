import time
import psycopg2
import mysql.connector
import pymongo
import redis

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

# Configurações de conexão para o MongoDB
mongodb_config = {
    'host': 'localhost',
    'port': 27017,
    'database': 'TestMongoDB',
    'user': '',
    'password': ''
}

# Configuração do Redis
redis_config = {
    'host': '127.0.0.1',
    'port': 6379,
    'password': ''
}

# Configurações de conexão para o MariaDB
maria_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'mariadb',
    'user': 'root',
    'password': ''
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

    # Instrução SQL para inserção no PostgreSQL
    sql = "INSERT INTO usuarios (nome, idade, email, senha) VALUES (%s, %s, %s, %s)"
    
    for _ in range(num_times):
        values = (name, idade, email, senha)
        cursor.execute(sql, values)
    
    connection.commit()
    cursor.close()
    connection.close()

def mysql_insert():
    connection = mysql.connector.connect(**mysql_config)
    cursor = connection.cursor()

    # Instrução SQL para inserção no MySQL
    sql = "INSERT INTO usuarios (nome, idade, email, senha) VALUES (%s, %s, %s, %s)"
    
    for _ in range(num_times):
        values = (name, idade, email, senha)
        cursor.execute(sql, values)
    
    connection.commit()
    cursor.close()
    connection.close()

def mongodb_insert():
    client = pymongo.MongoClient(host=mongodb_config['host'], port=mongodb_config['port'])
    db = client[mongodb_config['database']]
    collection = db['usuarios']

    for _ in range(num_times):
        document = {'nome': name, 'idade': idade, 'email': email, 'senha': senha}
        collection.insert_one(document)

    client.close()

def redis_insert():
    r = redis.Redis(**redis_config)
    for _ in range(num_times):
        key = f'user{_+1}'
        user_data = {
            'nome': name,
            'idade': 30,
            'email': email,
            'senha': senha
        }
        # Converter o dicionário em uma string
        user_data_str = str(user_data)
        r.set(key, user_data_str)


def maria_insert():
    connection = mysql.connector.connect(**maria_config)
    cursor = connection.cursor()

    # Instrução SQL para inserção no MariaDB (compatível com MySQL)
    sql = "INSERT INTO users (nome, idade, email, senha) VALUES (%s, %s, %s, %s)"
    
    for _ in range(num_times):
        values = (name, idade, email, senha)
        cursor.execute(sql, values)
    
    connection.commit()
    cursor.close()
    connection.close()

def add_data_to_databases(value, idade, email, senha, num_times):
    print("Inserindo dados em todos os bancos...")
    print()
    postgres_insert_time = measure_execution_time(postgres_insert)
    mysql_insert_time = measure_execution_time(mysql_insert)
    mongodb_insert_time = measure_execution_time(mongodb_insert)
    maria_insert_time = measure_execution_time(maria_insert)
    redis_insert_time = measure_execution_time(redis_insert)

    print("Tempo de inserção no PostgreSQL:", postgres_insert_time)
    print("Tempo de inserção no MySQL:", mysql_insert_time)
    print("Tempo de inserção no MongoDB:", mongodb_insert_time)
    print("Tempo de inserção no MariaDB:", maria_insert_time)
    print("Tempo de inserção no Redis:", redis_insert_time)


# Valores de exemplo para inserção
name = "Liedson"
idade = 30
email = "usuario@example.com"
senha = "senha123"
num_times = 10000

# Chamada da função para adicionar dados aos bancos de dados
add_data_to_databases(name, idade, email, senha, num_times)