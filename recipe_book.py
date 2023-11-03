def read_cookbook(file_name):
    cook_book={}
    with open(file_name, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            dish_name = lines[i].strip()
            ing_count = int(lines[i+1])
            ing_list = []
            for j in range(i+2, i+2+ing_count):
                ing_line = lines[j].strip().split(' | ')
                ing_list.append({'ingredient_name': ing_line[0], 'quantity': int(ing_line[1]), 'measure': ing_line[2]})
            cook_book[dish_name] = ing_list
            i += ing_count + 3
    return cook_book
file_name = r'ООП_ДЗ2\recipes.txt'
cook_book = read_cookbook(file_name)
# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list={}
    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
                else:
                    shop_list[ingredient_name]['quantity'] += quantity
        else:
            print(f"Блюдо {dish} отсутствует в cook_book")
    return shop_list

shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(shop_list)
        