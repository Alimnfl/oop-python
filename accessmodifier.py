# Access Modifier

# __ -> Private Access Modifier
#  _ -> Protected

class Player:
    # Attribute
    name = "Joni"
    __salary = 1_000_000 #private

    # Method
    def get_salary(self):
        return self.__salary

player = Player()
player.name = "Alimnfl"
player.__salary = 3_000_000

print(player.get_salary())
print(player.__salary)


# print(f"User {player.name} Berhasil Dibuat")

# player.name = "Alimnfl"
# print(f"Tapi {player.name} Ini adalah nama baru")