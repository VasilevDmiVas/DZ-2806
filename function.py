def print_users(local_users):
    if len(local_users) == 0:
        print('Коворкинг пуст')
        return
    index = 0
    for item in local_users:
        print(f'{index}) {item}')
        index += 1

def print_count_users(local_users):
    print(f'Количество посетителей: {len(local_users)}')

def add_users(local_users, local_max_users):
    if len(local_users) < local_max_users:
        local_user = input('Введите пользователя ')
        local_users.add(local_user)
    else:
        print('Коворкинг заполнен')

def remove_users(local_users):
    print(f'Удаление пользователя в коворкинге {local_users}')
    local_user = input('Введите пользователя которого удалить')
    local_users.remove(local_user)
