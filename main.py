import os
os.system("cls")


f = {
    "olma": [13000, 14000, 15000],
    "anor": [19000, 22000, 24000, 15000],
    "gilos": [6000, 9000, 5000, 4000],
    "banan": [30000, 28000]
}

for i in f:
    print(f"{i}:", int(sum(f[i])/len(f[i])))