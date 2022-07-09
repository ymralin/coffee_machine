recipes = [
    {
        'name': 'espresso',
        'water': 50,
        'coffee': 18,
        'milk': 0,
        'price': 1.50
     },
    {
        'name': 'latte',
        'water': 200,
        'coffee': 24,
        'milk': 150,
        'price': 2.50
     },
    {
        'name': 'cappuccino',
        'water': 250,
        'coffee': 24,
        'milk': 100,
        'price': 3.00
     }
]

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}


def report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee:"
          f"{resources['coffee']}ml\nMoney: ${resources['money']}")


def check_if_enough_resources(recipe):
    # this function checks if there is enough resources to serve selected coffee.
    # also returns price to avoid code repetition in separate function

    # find index of recipe in recipes list.
    i = None
    for index, element in enumerate(recipes):
        if element['name'] == recipe:
            i = index
    is_enough = True
    missing_resources = []
    if resources['water'] < recipes[i]['water']:
        missing_resources.append('water')
        is_enough = False
    if resources['milk'] < recipes[i]['milk']:
        missing_resources.append('milk')
        is_enough = False
    if resources['coffee'] < recipes[i]['coffee']:
        missing_resources.append('coffee')
        is_enough = False
    price = recipes[i]['price']
    return is_enough, missing_resources, price


def change_resources(selection):
    # find index of recipe in recipes list.
    i = None
    for index, element in enumerate(recipes):
        if element['name'] == selection:
            i = index
    # update resources counters
    for key in resources:
        if key != 'money':
            resources[key] -= recipes[i][key]
    resources['money'] += recipes[i]['price']


def insert_money():
    while True:
        try:
            quarters = int(input("How many quarters?: "))
            if quarters >= 0:
                break
        except ValueError:
            print("Wrong input")

    while True:
        try:
            dimes = int(input("How many dimes?: "))
            if dimes >= 0:
                break
        except ValueError:
            print("Wrong input")

    while True:
        try:
            nickles = int(input("How many nickles?: "))
            if nickles >= 0:
                break
        except ValueError:
            print("Wrong input")

    while True:
        try:
            pennies = int(input("How many pennies?: "))
            if pennies >= 0:
                break
        except ValueError:
            print("Wrong input")

    inserted_money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return round(inserted_money, 2)


def run_machine():
    coffee_types = []
    for el in recipes:
        coffee_types.append(el['name'])
    selection = ""
    while selection not in coffee_types:
        selection = input("What would you like? (espresso/latte/cappuccino):\n")
        if selection == "report":
            report()
        elif selection == "exit":
            quit()
    resources_check = check_if_enough_resources(selection)
    if not resources_check[0]:
        print(f"Not enough {resources_check[1]}")
        return None
    else:
        price = resources_check[2]
        print(f"Selected {selection}. Price: ${price}")
        print("Insert coins.")
        inserted_money = insert_money()
        needed = round(price - inserted_money, 2)
        while needed > 0:
            print(f"Not enough money. Inserted ${inserted_money}. Need ${needed} more.")
            inserted_money += insert_money()
            needed = round(price - inserted_money, 2)
        change = round(inserted_money - price, 2)
        if change > 0:
            print(f"Here is your${change} in change.")
        print(f"Here is your {selection}. Enjoy!")
        change_resources(selection)


running = True

while running:
    run_machine()
