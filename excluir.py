def exclui():
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
    
    busca = input("Digite o nome da tribo que deseja excluir: ")
    sql = "SELECT * FROM tb_indios WHERE nome_tribo LIKE %s"
    val = ("%" + busca + "%",)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    
    if result:
        cod = result[5]
        nome = result[0]
        confirmacao = input(f"Tem certeza que deseja deletar a tribo '{nome}'? (s/n) ")

        if confirmacao.lower() == "s":
            sql = "DELETE FROM tb_indios WHERE cod = %s"
            val = (cod,)
            cursor.execute(sql, val)
            con.commit()
            print("Item deletado com sucesso!")
        else:
            print("Operação cancelada pelo usuário")

    else:
        print("Erro, verifique os dados")
    con.close()
    
#exclui()
    