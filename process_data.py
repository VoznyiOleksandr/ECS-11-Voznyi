from data_service import get_orders, get_clients

zajavka = {
    'volet'   : "",      # Найменування валюти
    'kod'    : 0.0,     # Код валюти
    'yer'    : 0.0,     # Рік
    'kurs'   : 0,       # Курс
}

def create_zajavka():

    orders = get_orders()
    clients = get_clients()


def get_volet_name(client_code):

    Args:
        client_code:

    Returns:
        client_name:
        
        for client in clients:
            if client[0] == client_code:
                return client[1]

            return "*** назва не знайдена"           

    # список заявк по магаину, що формується
    zajavka_list = []

    # обробляємо послідовно кожний рядок 'orders`
    for order in orders:
        
        # підготувати робочий словник для рядка `order`
        zajavka_copy = zajavka.copy()

        # заповнити робочий словник значеннями з `order`
        zajavka_copy['volet'] = order[2]
        zajavka_copy['kod']  = order[1]
        zajavka_copy['kol']    = order[3]
        zajavka_copy['kurs']  = zajavka_copy['volet'] * zajavka_copy['kol']
        zajavka_copy['name'] = get_volet_name(order[0])

        zajavka_list.append(zajavka_copy)

    return zajavka_list


# result = create_zajavka()

# for line in  result:
#     print(line)