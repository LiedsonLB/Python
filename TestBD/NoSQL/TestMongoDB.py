import time
import pymongo

# Configurações de conexão para o MongoDB
mongodb_config = {
    'host': 'localhost',
    'port': 27017,
    'database': 'TestMongoDB',
    'user': '',
    'password': ''
}

def measure_execution_time(operation):
    start_time = time.time()
    operation()
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

def mongodb_insert():
    client = pymongo.MongoClient(host=mongodb_config['host'], port=mongodb_config['port'])
    db = client[mongodb_config['database']]
    collection = db['TesteDeDB']

    for _ in range(num_times):
        document = {'nome': value}
        collection.insert_one(document)

    client.close()

# Valores de exemplo para inserção
value = "Liedson"
num_times = 10

# Medição do tempo de inserção
mongodb_insert_time = measure_execution_time(mongodb_insert)

# Exemplo de saída do tempo de execução
print("Tempo de inserção no MongoDB:", mongodb_insert_time)
