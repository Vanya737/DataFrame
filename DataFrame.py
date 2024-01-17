import pandas as pd

data = pd.read_csv("data.csv", delimiter=";",
                   names=['Character_name', 'Character_force', 'Weapon_damage', 'Damage_reflection'])
print(data)

def job():
    Enter_1 = str(input("Enter сolumn name"))
    Enter_2 = int(input("Enter cell number"))

    print(data.at [Enter_2, Enter_1])


job()






