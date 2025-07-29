import os
os.system("cls")

car = {
    "brand": "BMW",
    "model": "M8",
    "price": 215000,
    "speed": 330,
    "mileage": 0,
    "year": 2023,
}

# print(car['brant'])
# print(car.get('bran', f"Xato kalit, {car.keys()}"))

# print(car.keys())

# print(car.values())

# car.pop('year')
# print(car)

# print(car.items())
# for k,q in car.items():
#     print(k, q)

# car.popitem()
# print(car)

# car['price'] = 88000
# car["mileage"] = 4000
# car['color'] = 'red'
car.update({"price": 88000, 'mileage':4000, 'color':'red'})
print(car)