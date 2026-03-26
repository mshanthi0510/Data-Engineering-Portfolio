zomato_favourites = {"Briyani": 140,"Parotta" : 60,"Fried_rice": "120"}
swiggy_favourites = {"Naan":60,"Panner Butter masala":456,"Dosa":120}
domino_favourites = {"cheese burst pizza":134,"garlic bread":90,"paneer pockets":80}

def zomato_app(price,discount = 10):
    return f"zomato_app discount {price-discount}"

def swiggy_app(price,discount = 12):
    return f"swiggy_app discount {price-discount}"

def dominoz_app(price,discount = 45):
    return f"dominoz_app discount {price-discount}"

def HOF(price,app_func):
    return app_func(price)

def best_deal(price1,price2,price3):
    return min(zomato_app(price1),swiggy_app(price2),dominoz_app(price3))

print(HOF(zomato_favourites["Briyani"],zomato_app))
print(HOF(swiggy_favourites["Naan"],swiggy_app))
print(HOF(domino_favourites["paneer pockets"],dominoz_app))
print("The best deal from overall app discount is",
best_deal(zomato_favourites["Briyani"],swiggy_favourites["Naan"],
domino_favourites["paneer pockets"]))

