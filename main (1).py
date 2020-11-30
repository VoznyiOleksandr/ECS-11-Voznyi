"""головний модуль додатку
виводить розрахункову таблицю, зберігає розрахунок у файлі,
показує на екрані первинні дані
"""
import os
from process_data import create_orders_list
from data_service import show_clients, show_orders, get_orders, get_clients

MAIN_MENU = \
"""
~~~~~~~~~~~~~~~~~~~~~ ОБРОБКА ЗАЯВОК НА Найменування валюти  ~~~~~~~~~~~~~~~~~~~~

1 - вивід заявок на екран
2 - запис заявок в файл
3 - вивід списка накладних
4 - вивід довідника Код валюти
0 - завершити роботу
---------------------------------
"""

TITLE = 'ЗАЯВКА НА Найменування валюти  ПО МАГАЗИНУ'

HEADER = \
"""
=======================================================================
|  Найменування валюти      |   Код валюти      | Рік |Курс на 1.10  | 
========================================================================
"""

STOP_MESSAGE = "Для продовження натисніть <Enter>"

FOOTER = \
"""
=====================================================================================

"""
def show_orders(orders_list):
    """вивод на екран розрахункової таблиці

    Args:
        orders_list ([type]): список заявок
    """
    print(f"\n\n{TITLE:^86}")
    print(HEADER)
    
    for orders in orders_list:
        print(f"{orders['volet']:22}", 
              f"{orders['kod']:17}",
              f"{orders['kurs']:^10}",
              f"{orders['kol']:8}",
              f"{orders['name']:>11.2f}"
              )
     
    print(FOOTER)   

def write_file(orders_list):
    """запис списку заявок в файл

    Args:
        orders_list ([type]): список заявок
    """
    with open('./data/orders.txt', "w") as orders_file:
        for orders in orders_list:
            line = \
                orders['volet']     + ';'      + \
                orders['kod']       + ';'      + \
                str(orders['kurs']) + ';'      + \
                str(orders['kol'])  + ';'      + \
                str(orders['name']) + ';'      + '\n'
            
            orders_file.write(line)
    
    print("Файл успішно сформовано ...")
            

while True:
    os.system('clear')
    print(MAIN_MENU)
    command_number = input('Введіть номер команди: ')
    
    # обробка команд користувача
    if command_number == '0':
        print("\nПрограма завершила роботу")
        exit(0)
    
    elif command_number == '1':
        orders_list = create_orders_list()
        show_orders(orders_list)
        input(STOP_MESSAGE)
        
    elif command_number == '2':
        orders_list = create_orders_list()
        write_file(orders_list)
        input(STOP_MESSAGE)
        
    elif command_number == '3':
        orders = get_orders()
        show_orders(orders)
        input(STOP_MESSAGE)
        
    elif command_number == '4':
        clients = get_clients()
        show_clients(clients)
        input(STOP_MESSAGE)
        

        
    