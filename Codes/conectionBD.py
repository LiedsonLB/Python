import mysql.connector

con = mysql.connector.connect(host='localhost', database='db_contas', user='root', password='')
cursor = con.cursor()
if con.is_connected():
    db_info = con.get_server_info()
    print('conectado ao servidor MYSQL versão ', db_info)
    cursor.execute("SELECT database();")
    banco = cursor.fetchone()
    print("conectado ao banco de dados ", banco)

if con.is_connected():
    cursor.close()
    con.close()
    print("conexão encerrada")