import os
from pprint import pprint


def dict_collector():
    file_path = os.path.join(os.getcwd(), 'recipies.txt')
    cook_book = {}
    with open(file_path, encoding='utf-8') as file_work:
        for line in file_work:
            dish_name = line.strip()
            counter = int(file_work.readline().strip())
            list_of_ingredient = []
            for i in range(counter):
                dish_items = {}
                ingredient = file_work.readline().strip().split(' | ')
                dish_items['ingredient_name'], dish_items['quantity'], dish_items['measure'] = ingredient
                list_of_ingredient.append(dish_items)
            file_work.readline()
            cook_book[dish_name] = list_of_ingredient
        return cook_book


def get_shop_list_by_dishes(dishes, pers_count):
    ingr_list = dict()

    for dish_name in dishes:
        if dish_name in cook_book:
            for ings in cook_book[dish_name]:
                order_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    order_list['measure'] = ings['measure']
                    order_list['quantity'] = int(ings['quantity']) * pers_count
                    ingr_list[ings['ingredient_name']] = order_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     int(ings['quantity']) * pers_count
        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingr_list


cook_book = dict_collector()
pprint(dict_collector())
print(('--------------'))
pprint(get_shop_list_by_dishes(dishes=['Омлет', 'Омлет'], pers_count=2))
