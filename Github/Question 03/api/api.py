# Faça um relatório sobre os funcionários da Radix que estão registrados
# no banco de dados a partir dos registros existentes no banco de dados
# com a seguinte estrutura:

# Seu trabalho, agora é selecionar todos os funcionários que residem no
# Rio de Janeiro, possuir mais de 20 anos e já trabalhar em mais de 3
# projetos finalizados
# conectanto...
import sqlite3
from datetime import date
from date_base_generator import read_table_01
from date_base_generator import read_table_02
from date_base_generator import read_table_03

# conectanto...
conn = sqlite3.connect('radix.db')
#definindo um cursor
cursor = conn.cursor()

funcionarios = read_table_01()
projetos = read_table_02()
fun_pro = read_table_03()


def find_estado(uf):
    # busca apenas os funcionários do estado indicado
    uf = uf.upper()
    x = []
    for i in range(len(funcionarios)):
        if funcionarios[i][2] == uf:
            x.append(funcionarios[i])
    return x


def find_idade_20(func):
    # busca todos os funcionários com mais de 20 anos
    year_20 = (date.today().year)-20
    x = []
    for i in range(len(func)):
        if func[i][3] <= year_20:
            x.append(func[i])
    return x


def find_finished_project():
    # código está errado
    id = 'xx/xx/xxxx'
    # localiza apenas projeto finalizado
    x = cursor.execute(
        'SELECT * FROM projeto WHERE date_fim = ?', (id,))
    if x.fetchone() ==  None:
        return 'Em andamento'
    
    pass


def proj(func):
    # localiza todos os projetos e funcionários que trabalharam nele.
    # filtra os que participaram de no mínimo 3 projetos
    x = []  # irá receber id de todos os funcionário que moram no rio e tem mais de 20 anos
    func_3 = []  # irá receber os funcionários com mais de 3 projetos
    y = []
    for i in range(len(func)):
        x.append(func[i][0])

    # filtro para apenas os que tem mais de 3 projetos
    for j in range(len(x)):
        z = 0
        y = []
        for k in range(len(fun_pro)):
            if x[j] == fun_pro[k][0]:
                y.append(fun_pro[k])
                z+=1
        if z >= 3:
            func_3.append(y)

    # vou cruzar os projetos finalizados
    

    return func_3


print((date.today().year)-20)
print(find_finished_project())
# print(find_estado('RJ'))
# print(find_idade_20(find_estado('rj')))
# print(proj(find_idade_20(find_estado('rj'))))
# print(fun_pro)
conn.close()