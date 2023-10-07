import time
import redis

# Configuração do Redis
redis_config = {
    'host': '127.0.0.1',
    'port': 6379,
    'password': ''
}

def measure_execution_time(operation):
    start_time = time.time()
    operation()
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time


def add_data_to_redis(value, num_times):
    print("Inserindo dados no Redis...")
    print()

    # Medição do tempo de inserção no Redis
    redis_insert_time = measure_execution_time(redis_insert)

    # Imprime o tempo de inserção no Redis
    print("Tempo de inserção no Redis:", redis_insert_time)

# Valor de exemplo para inserção
value = "Liedson"

# Número de vezes que o dado será adicionado
num_times = 10

# Chamada da função para adicionar dados ao Redis
add_data_to_redis(value, num_times)

