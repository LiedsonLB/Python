import time
import mysql.connector

mysql_config = {
    'host': 'localhost',
    'port': 3306,
    'database': 'experimentodb',
    'user': 'root',
    'password': '',
    'charset': 'utf8mb4'
}

def measure_execution_time(operation):
    start_time = time.time()
    operation()
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

def mysql_insert():
    connection = mysql.connector.connect(**mysql_config)
    cursor = connection.cursor()
    # Execute a operação de inserção no MySQL
    cursor.execute("INSERT INTO teste (nome) VALUES (%s)", ('Liedson',))
    connection.commit()
    cursor.close()
    connection.close()

# Valor de exemplo para inserção
value1 = "Liedson"
value2 = "Value 2"

# Medição do tempo de inserção no MySQL
mysql_insert_time = measure_execution_time(mysql_insert)

# Exemplo de saída do tempo de execução
print("Tempo de inserção no MySQL:", mysql_insert_time)

mysql_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'experimentodb',
    'user': 'root',
    'password': ''
}
