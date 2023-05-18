#Essa é a função de exibir

def exibe():
    import mysql.connector

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
        
    comando = "Select * from tb_indios"
    cursor = con.cursor()
    cursor.execute(comando)
    result = cursor.fetchall()
    for linhas in result:
        print(linhas)
        
    con.close()

#exibe()