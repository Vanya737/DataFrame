import pandas as pd

data = pd.read_csv("data.csv", delimiter=";",
                   names=['Character_name', 'Character_force', 'Weapon_damage', 'Damage_reflection'])
print(data)

while True:
    def job():
        Enter_1 = str(input("Enter сolumn name"))
        Enter_2 = int(input("Enter cell number"))

        print(data[Enter_1].values[Enter_2])


    job()






