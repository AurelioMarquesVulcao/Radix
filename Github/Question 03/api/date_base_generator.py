import sqlite3
import random
import form_generator as gen


# conectanto...
conn = sqlite3.connect('radix.db')
#definindo um cursor
cursor = conn.cursor()
# ----------------------------------------------------------------------------------------------------------------------------------
# criar uma classe e isolar as funções que criam os bancos.
# ----------------------------------------------------------------------------------------------------------------------------------

# criando a tabela(schema)
def create_tables01():
    cursor.execute("""
        CREATE TABLE funcionario (
            id_funcionario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            uf VARCHAR(2) NOT NULL,
            ano_nascimento DATE NOT NULL
    );
    """)


def create_tables02():
    cursor.execute("""
        CREATE TABLE projeto (
            id_projeto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            dada_inicio DATE NOT NULL,
            data_fim DATE NOT NULL    
            
    );
    """)


def create_tables03():
    cursor.execute("""
        CREATE TABLE funcionario_projeto (
            id_funcionario INTEGER NOT NULL,
            id_projeto INTEGER NOT NULL
    
    );
    """)


# -------------------------------------------------------------------------------------------------------------------------------------------
def create_function():
    # Populate the database with employee data.
    # Preencher o banco de dados com dados dos funcionários.
    funcionarios = []
    # I must fill in the loop with the desired number of employees.
    # Devo preencher o laço com a quantidade de funcionários desejados.
    for c in range(50):
        funcionarios += [(gen.random_name(), gen.random_estate(), gen.random_birth())]
    # inserindo dados na tabela
    cursor.executemany("""
    INSERT INTO funcionario (nome, uf, ano_nascimento)
    VALUES (?,?,?)
    """, funcionarios)

    conn.commit()
    # return funcionarios


def create_project():
    # Populates the database with project data.
    # Preenche o banco de dados com os dados dos projetos.
    projetos = []
    for c in range(5):
        start = gen.random_start_date()
        end = gen.random_end_date(start)
        projetos += [(f'Projeto_0{c+1}', start, end)]
    # inserindo dados na tabela
    cursor.executemany("""
    INSERT INTO projeto (nome, dada_inicio, data_fim)
    VALUES (?,?,?)
    """, projetos)

    conn.commit()


def create_project_function():
    # Populates the database with employees and projects associated with these employees.
    # Preenche o banco de dados com funcionários e projetos associados a estes funcionários.
    proj_fun = []
    # vou criar um lista que repete o numero de funcionários 6 vezes, para combinar equipes
    # de 6 funcionários aos projetos.
    a = [] # id de funcionario
    x = [] # id de projeto
    '''proj_fun = [(2,2), (2,5), (3,9), (3,4)]'''  # necessario para testar o banco com poucos dados --apagar--
    
    proj_fun = []
    b = 1
    for i in read_table_01():
        a = b
        b+=1
        for j in range(1, random.randint(1,6)): 
            x = random.randint(1,len(read_table_02()))
            proj_fun += [(a, x)]
        
    # inserindo dados na tabela
    cursor.executemany("""
    INSERT INTO funcionario_projeto (id_funcionario, id_projeto)
    VALUES (?,?)
    """, proj_fun)

    conn.commit()


def delete_functionary(id):
    # excluindo um registro da tabela
    cursor.execute("""
    DELETE FROM funcionario
    WHERE id_funcionario = ?
    """, (id,))

    conn.commit()

    #print('Registro excluido com sucesso.')

    conn.close()


def delete_project(id):
    # excluindo um registro da tabela
    cursor.execute("""
    DELETE FROM projeto
    WHERE id_projeto = ?
    """, (id,))

    conn.commit()

    #print('Registro excluido com sucesso.')

    conn.close()


def delete_functionary_project(id):
    # excluindo um registro da tabela
    cursor.execute("""
    DELETE FROM funcionario_projeto
    WHERE id_projeto = ?
    """, (id,))

    conn.commit()

    #print('Registro excluido com sucesso.')

    conn.close()


def read_table_01():
    # lendo os dados
    cursor.execute("""
    SELECT * FROM funcionario;
    """)

    table = []
    for linha in cursor.fetchall():
        #print(linha)
        table.append(linha)

    return table
    conn.close()    


def read_table_02():
    # lendo os dados
    cursor.execute("""
    SELECT * FROM projeto;
    """)

    table = []
    for linha in cursor.fetchall():
        #print(linha)
        table.append(linha)

    return table
    conn.close()


def read_table_03():
    # lendo os dados
    cursor.execute("""
    SELECT * FROM funcionario_projeto;
    """)

    table = []
    for linha in cursor.fetchall():
        #print(linha)
        table.append(linha)

    return table
    conn.close()


def localizar_cliente( id):
    r = cursor.execute(
        'SELECT * FROM funcionario WHERE id_funcionario = ?', (id,))
    return r.fetchone()


# create_tables01()
# create_tables02()
# create_tables03()


# create_function()
# create_project()
# create_project_function()


# print(read_table_01(), "-"*70 )
# print(read_table_02(), "-"*70)
# print(read_table_03(), "-"*70)


# delete_functionary(5)
# delete_project(5)
# delete_functionary_project(1)


# conn.close()
