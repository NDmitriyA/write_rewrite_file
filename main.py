import os


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


print(dict_collector())
