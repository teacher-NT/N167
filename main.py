import os
os.system("cls")

with open("N167/image.jpeg", "rb") as file:
    data = file.read()
    print(len(list(data)))
    # for i in list(data):
    #     print(i, end=" ")