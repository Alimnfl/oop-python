class Player:
    # Init supaya otomatis init yang dijalankan
    def __init__(self, name, health = 100, energy = 100) :
        self.health = health
        self.energy = energy
        self.name = name
    
    def attack(self, target, damage = 1 ):
        target.health -= damage
        self.energy -= damage # Jadi self.energy = self.energy -  damage
        print(f"{self.name} Attacking {damage} damage to {target.name}")
        if target.is_attacked(player_name = self.name):
            self.health -= target.damage
        # print(f"Attacking to monster, Monster health: {target.health} left & your energy is: {self.energy} left")

    def show_info(self):
        print(f"{self.name} Health: {self.health}")
        print(f"{self.name} Energy: {self.energy}")

class Monster:
    #init
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health #dinamis
        self.health_init = self.health #akan selalu 500
        self.damage = 10
        # print(f"Monster Created!")

    def is_attacked(self, player_name):
        print(f"{self.name} Attacked back {self.damage} damage to {player_name} ")
        if self.health < self.health_init: #misal darah sisa 420 < 500
            return self.health < self.health_init   

    def show_info(self):
        print(f"{self.name} Health: {self.health}")


player1 = Player(name="Alimnfl")
player2 = Player(name="Raza")
dragon = Monster(name="Balmond", health=500)
scorpion = Monster(name="Scurpy Darat", health=500)

player1.attack(target = dragon, damage=80)
player2.attack(target = scorpion, damage=30)

player1.show_info()
player2.show_info()
dragon.show_info()
scorpion.show_info()

#Tambahan penyerangan
# player.attack()
# player.attack()

# print(player.__dict__)