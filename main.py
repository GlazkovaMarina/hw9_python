# # 3 Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, в котором каждый элемент списка является и ключом и значением. 
# # Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.
# def to_dict(lst):
#     new_dict = {}
#     for elem in lst:
#         new_dict[elem] = elem
#     return new_dict

# lst = ["1", "two", "3", "four", "5"]
# print(to_dict(lst))

# # 4. Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs),
# # которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict,
# #  состоящий всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.

# my_dict = {"first_one": "we can do it"}

# def biggest_dict(**kwargs):
#     global my_dict
#     for key in kwargs:
#         my_dict[key] = kwargs[key]
#     return my_dict

# biggest_dict(one=1, two=2, three=3, four = 4)
# biggest_dict(five=5)
# print(biggest_dict(six=6, seven=7, eight=8))

