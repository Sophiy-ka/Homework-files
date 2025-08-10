def cook_book(recipes):
    cook_book = {}
    with open('resipes.txt', 'r', encoding='utf-8') as file:
        while True:
            recipe_name = file.readline().strip()
            if not recipe_name:
                break
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_info = file.readline().strip().split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_info[0],
                'quantity': int(ingredient_info[1]),
                'measure': ingredient_info[2]
            })
            cook_book[recipe_name] = ingredients
            file.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                if name not in shop_list:
                    shop_list[name] = {
                        'measure': ingredient['measure'],
                        'quantity': ingredient['quantity'] * person_count
                    }
                else:
                    shop_list[name]['quantity'] += ingredient['quantity'] * person_count
    return shop_list

cook_book = read_recipes('recipes.txt')