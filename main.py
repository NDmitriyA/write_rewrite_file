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


def rewrite_file(path1=None, path2=None, path3=None):
    if path1 or path2 or path3 is None:
        path1 = 'text1.txt'
        path2 = 'text2.txt'
        path3 = 'text3.txt'
        os.chdir('TEXT')
        final_file = 'final_file.txt'
        f1_path = os.path.join(os.getcwd(), path1)
        f2_path = os.path.join(os.getcwd(), path2)
        f3_path = os.path.join(os.getcwd(), path3)
        with open(f1_path, encoding='utf-8') as fp1, open(f2_path, encoding='utf-8') as fp2, open(f3_path,
                                                                                                  encoding='utf-8') as fp3:
            file1 = fp1.readlines()
            file2 = fp2.readlines()
            file3 = fp3.readlines()
        with open(final_file, 'w', encoding='utf-8') as f_f:
            if len(file3) > len(file1) < len(file2) < len(file3):
                f_f.write(path1 + '\n' + str(len(file1)) + '\n')
                f_f.writelines(file1)
                f_f.write('\n')
                f_f.write('\n' + path2 + '\n' + str(len(file2)) + '\n')
                f_f.writelines(file2)
                f_f.write('\n')
                f_f.write('\n' + path3 + '\n' + str(len(file3)) + '\n')
                f_f.writelines(file3)
            elif len(file2) > len(file1) < len(file3) < len(file2):
                f_f.write(path1 + '\n' + str(len(file1)) + '\n')
                f_f.writelines(file1)
                f_f.write('\n')
                f_f.write('\n' + path3 + '\n' + str(len(file3)) + '\n')
                f_f.writelines(file3)
                f_f.write('\n')
                f_f.write('\n' + path2 + '\n' + str(len(file2)) + '\n')
                f_f.writelines(file2)
            elif len(file1) > len(file2) < len(file3) < len(file1):
                f_f.write(path2 + '\n' + str(len(file2)) + '\n')
                f_f.writelines(file2)
                f_f.write('\n')
                f_f.write('\n' + path3 + '\n' + str(len(file3)) + '\n')
                f_f.writelines(file3)
                f_f.write('\n')
                f_f.write('\n' + path1 + '\n' + str(len(file1)) + '\n')
                f_f.writelines(file1)
            elif len(file1) > len(file2) < len(file3) > len(file1):
                f_f.write(path2 + '\n' + str(len(file2)) + '\n')
                f_f.writelines(file2)
                f_f.write('\n')
                f_f.write('\n' + path1 + '\n' + str(len(file1)) + '\n')
                f_f.writelines(file1)
                f_f.write('\n')
                f_f.write('\n' + path3 + '\n' + str(len(file3)) + '\n')
                f_f.writelines(file3)
            elif len(file2) > len(file3) < len(file1) < len(file2):
                f_f.write(path3 + '\n' + str(len(file3)) + '\n')
                f_f.writelines(file3)
                f_f.write('\n')
                f_f.write('\n' + path1 + '\n' + str(len(file1)) + '\n')
                f_f.writelines(file1)
                f_f.write('\n')
                f_f.write('\n' + path2 + '\n' + str(len(file2)) + '\n')
                f_f.writelines(file2)
            else:
                f_f.write(path3 + '\n' + str(len(file3)) + '\n')
                f_f.writelines(file3)
                f_f.write('\n')
                f_f.write('\n' + path2 + '\n' + str(len(file2)) + '\n')
                f_f.writelines(file2)
                f_f.write('\n')
                f_f.write('\n' + path1 + '\n' + str(len(file1)) + '\n')
                f_f.writelines(file1)


cook_book = dict_collector()
pprint(dict_collector())
print(('--------------'))
pprint(get_shop_list_by_dishes(dishes=['Омлет', 'Омлет'], pers_count=2))
rewrite_file()
