pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}

recipes = {
    "Butter chicken": [
        "chicken",
        "lemon",
        "cumin",
        "paprika",
        "chilli powder",
        "yogurt",
        "oil",
        "onion",
        "garlic",
        "ginger",
        "tomato puree",
        "almonds",
        "rice",
        "coriander",
        "lime",
    ],
    "Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on toast": [
        "beans",
        "bread",
    ],
    "Spam a la tin": [
        "spam",
        "tin opener",
        "spoon",
    ],
}

dict_menu = {}
for key, value in enumerate(recipes):
    dict_menu[str(key + 1)] = value
while True:
    print("please choose recipe")
    print("--------------------")
    for key, value in dict_menu.items():
        print(f"{key}-{value}")
    choice = input(": " )
    if choice == "0":
        break
    elif choice in dict_menu:
        selected_item = dict_menu[choice]
        print(f"you choose {selected_item}")
        ingredients = recipes[selected_item]
        print(ingredients)
        print("please choose from the ingrediants")
    food_shelf = input(":  " )
    for food_shelf in ingredients:
        if food_shelf in pantry:
                print(f"you've got {food_shelf} from pastery")
        elif food_shelf not in pantry:
            print(f"{food_shelf} not included in pantery")
 
            

    

        


