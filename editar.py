def edita():
    
    import mysql.connector
    x = 0
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
    busca = input("Digite o nome da tribo que deseja editar: ")
    sql = "SELECT * FROM tb_indios WHERE nome_tribo LIKE %s"
    val = ("%" + busca + "%",)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    
    
    if result:
        cod = result[5]
        nome_antigo = result[0]
        hab_ant = result[1]
        ren_ant = result[2]
        esc_ant = result[3]
        tra_ant = result[4]
        
        print(result,"\nO que você deseja editar? (Digite o número)")
        print("1 - Nome da tribo")
        print("2 - Habitantes")
        print("3 - Renda")
        print("4 - Escolaridade")
        print("5 - Trabalho")
        op = int(input(""))
        
        if op == 1:
            print(f"O nome atual da tribo é '{nome_antigo}'.")
            novo_nome = input("Digite o novo nome: ")
            sql = "UPDATE tb_indios SET nome_tribo = %s WHERE cod = %s"
            val = (novo_nome, cod)
            cursor.execute(sql, val)
            con.commit()
        
        
        elif op == 2:
            print(f"O número de habitantes atual da tribo é '{hab_ant}'.")
            novo_hab = input("Digite o novo número: ")
            sql = "UPDATE tb_indios SET n_habitante = %s WHERE cod = %s"
            val = (novo_hab, cod)
            cursor.execute(sql, val)
            con.commit()
            
            
        elif op == 3:
            print(f"O número de habitantes atual da tribo é '{ren_ant}'.")
            novo_ren = input("Digite o novo número: ")
            sql = "UPDATE tb_indios SET renda_media_mensal = %s WHERE cod = %s"
            val = (novo_ren, cod)
            cursor.execute(sql, val)
            con.commit()
            
            
        elif op == 4:
            print(f"O número de habitantes atual da tribo é '{esc_ant}'.")
            novo_esc = input("Digite o novo número: ")
            sql = "UPDATE tb_indios SET escolaridade = %s WHERE cod = %s"
            val = (novo_esc, cod)
            cursor.execute(sql, val)
            con.commit()
            
            
        elif op == 5:
            print(f"O número de habitantes atual da tribo é '{tra_ant}'.")
            novo_tra = input("Digite o novo número: ")
            sql = "UPDATE tb_indios SET trabalho = %s WHERE cod = %s"
            val = (novo_tra, cod)
            cursor.execute(sql, val)
            con.commit()
            
            
        else:
            x = 5
            print("ERRO")
            
        
        if x != 5:
            print("Item atualizado com sucesso!")
        else:
            print("Operação cancelada")
            
    else:
        print("Não foi encontrado nenhum registro com o nome informado.")
    
    con.close()
    
#edita()
