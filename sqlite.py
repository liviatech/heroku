import sqlite3

banco = sqlite3.connect('banco_na_hora.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE login( nome tex, sobrenome tex, nick tex, datanascimento integer , dependentes integer, telefone integer, email tex, senha tex, genero text)")

cursor.execute("INSERT INTO login VALUES('Maria', 'silva', 'ffffff', 11001010, 2, 11010101111, 'maria@gmail.com', 'teste', 'feminino' )")



banco.commit()



