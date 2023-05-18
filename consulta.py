def consulta():
    
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
        
    cursor = con.cursor()
    busca = input("Digite o nome da tribo que deseja cunsultar: ")
    sql = "SELECT * FROM tb_indios WHERE nome_tribo LIKE %s"
    val = ("%" + busca + "%",)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    print(result)
    
    con.close()
    
