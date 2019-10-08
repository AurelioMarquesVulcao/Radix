import sqlite3
import random
import names
from datetime import datetime



def random_estate():
    # Generates a state randomly.
    # Gera um estado aleatoriamente.
    estate = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 
    'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
    estate = ['RJ']
    return random.choice(estate)
   

def random_name():
    # Generates a name randomly.
    # Gera um nome aleatóriamente.
    return names.get_full_name()


def random_birth():
    # Generates one year of birth.
    # Gera um ano de nascimento.
    return random.randint(1990, 2001)


def random_start_date():
    # Generates a start date for the project.
    # Gera uma data para o início do projeto.
    months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    b = random.randint(1, 12)
    a = random.randint(1, months[b])
    c = random.randint(1990, 2001)
    date = (f'{a}/{b}/{c}')
    return date
    


def random_end_date(i):
    # Generates a project end date from the start date.
    # Gera uma data para o fim do projeto à partir da data de início.
    months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    i = i.split('/')
    # b = int(a[0]), int(a[1]) + random.randint(1, 12), int(a[2])
    # b irá gerar um adicinal de meses ao projeto
    i[2] = int(i[2])
    month_02 = ''
    
    month_01 = (int(i[1]) + random.randint(1, 12))
    
    if month_01 > 12:
        i[2] + 1
        month_02 =  month_01//12
    else:
        month_02 = month_01

    a =  random.randint(1, months[month_02])
    c = i[2] + random.randint(0, 1)
    date = (f'{a}/{month_02}/{c}')
    #return date
    return date #month_02


def random_functionary_project():
    # Associates an functionary id with a project.
    # Associa o id de um funcionário a um projeto.
    # project = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    pass


def type_date_time(a):
    # Converts to a date time class
    # Converte para uma classe date time
    str_date = a

    date = datetime.strptime(str_date, '%d/%m/%Y').date()

    print(date, type(date))



# print(random_estate())
# print(random_name())
# print(random_birth())
''' a = random_start_date()
print(a)
b = random_end_date(a)
print(b) '''
# print(random_functionary_project())
