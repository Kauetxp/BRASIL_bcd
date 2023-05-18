#Comando de inserção

def insere():
    import mysql.connector
    import random
    config = {
        "user":"admin", 
        "password":"grunge1994", 
        "host" : "bdbrasil.ce1nbzgrn5ab.us-east-1.rds.amazonaws.com", 
        "database":"Brasil"
    }
    
    try:
        con = mysql.connector.connect(**config)
        print("Conexão com banco executada com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro de conexão: {err} ")
        
    cursor = con.cursor()
        
    n_tribo = input("Nome da tribo: ")
    n_habita = input("Numero de habitantes: ")
    renda = input("Renda média: ")
    escol = input("Escolaridade: ")
    trabalho = input("Trabalho (sim/nao): ")
    cod = (random.randint(0,1000000) - random.randint(0,100))
    comando = "INSERT INTO tb_indios VALUES (%s, %s,%s, %s,%s,%s)"
    val = (n_tribo,n_habita,renda,escol,trabalho,cod)
    cursor.execute(comando, val)
    
    con.commit()
    
    print(cursor.rowcount, "registro(s) inserido(s) com sucesso.")
    
    con.close()
    
#insere()