"""модуль зчитує первинні файли для обробки
"""

def get_clients():
    
    with open("./data/clients.txt") as clients_file:
        from_clients = clients_file.readlines() 

    
    clients_list = []

    for line in from_clients:
        line_list = line.split(';')
        clients_list.append(line_list)


    return clients_list


def get_orders():

    with open('./data/orders.txt') as orders_file:
        from_orders = orders_file.readlines()



    orders_list = []

    for line in from_file:
        line_list = line.split(';')
        orders_list.append(line_list)

    return orders_list 


def show_clients(clients):

    clients_code_from = input("З якого кода клієнта? ")
    clients_code_to   = input("По який кода клієнта? ")   

    kol_lines = 0

    for cod in clients:
        if clients_code_from <= client[0] <= clients_code_to:
            print ("код:{:5} Курс1:{:15} Курс2:{:25} Курс3:{:25} Рік:{:25}".format(cod[0], cod[1], cod[2], cod[3], cod[4].rstrip()))
            kol_lines = kol_lines + 1

        if lines_found == 0
            print("Записів з кодом від {} до {} не знайдено".format(dovidnik_code_from, dovidnik_code_to))


def show_orders(orders):

    orders_code_from = input("З якого коду товарної групи?")
    orders_code_to = input("По який код товарної групи?")

    kol_lines = 0

    for cod in tovaroobig: 
        if tovaroobig_code_from <= cod[0] <= tovaroobig_code_to:
        print("Найменування валюти: {:6} Код валюти: {:4} Рік: {:4} Курс: {:4}"
            .format(order[0], order[1], order[2], order[3].rstrip()))
           
            kol_lines = kol_lines + 1

    if kol_lines == 0:
        print("Записів з кодом від {} до {} не знайдено".format(tovaroobig_code_from, tovaroobig_code_to))        


    






