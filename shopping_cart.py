
products = ['tomatoes', 'bananas', 'eggs']
prices = [2.99, 1.5, 1.99]

def calculate_total():
    return sum(shopping_cart.values())

shopping_cart = {}

def add_item():
    while True:
        item = input("Enter a key item (or 'done' to stop): ")
        if item.lower() == 'done':
            break
        item_value = input(f"Enter the price/value for {item}: ")
        shopping_cart.update({item: item_value})
    return shopping_cart

add_item()
print("Final Cart:", shopping_cart)
total = calculate_total()
print(total)