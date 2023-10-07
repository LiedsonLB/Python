import time
import mysql.connector

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

def maria_insert():
    connection = mysql.connector.connect(**maria_config)
    cursor = connection.cursor()
    
    for _ in range(num_times):
        cursor.execute("INSERT INTO users (nome) VALUES (%s)", (value,))
    
    connection.commit()
    cursor.close()
    connection.close()

def add_data_to_database(value, num_times):
    print("Inserindo dados no banco de dados...")
    print()

# Valores de exemplo para inserção
value = "Liedson"

# Número de vezes que o dado será adicionado
num_times = 10

# Medição do tempo de inserção no MariaDB
maria_insert_time = measure_execution_time(maria_insert)

# Imprime o tempo de inserção no MariaDB
print("Tempo de inserção no MariaDB:", maria_insert_time)

# Chamada da função para adicionar dados ao banco de dados
add_data_to_database(value, num_times)