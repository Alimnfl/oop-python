# Access Modifier

class Player:
    # Init supaya otomatis init yang dijalankan
    def __init__(self, health = 100, energy = 100) :
        self.health = health
        self.energy = energy
        # print(f"Player Created!")
        # print(f"Player Created!, Health = {self.health}" )
    
    def attack(self, target, damage = 1 ):
        target.health -= damage
        self.energy -= damage # Jadi self.energy = self.energy -  damage
        print(f"Attacking to monster, Monster health: {target.health} left & your energy is: {self.energy}")


class Monster:
    #init
    def __init__(self, health = 100):
        self.health = health #dinamis
        self.health_init = self.health #akan selalu 500
        # print(f"Monster Created!")

    def attack(self):
        if self.health < self.health_init: #misal darah sisa 420 < 500
            print("Dragon siap serang kembali")
        else:
            print("Dragon turu dulu ga sih....")        


player1 = Player()
player2 = Player()
dragon = Monster(health=700)

player1.attack(target = dragon, damage=80)
player2.attack(target = dragon, damage=30)

dragon.attack()

#Tambahan penyerangan
# player.attack()
# player.attack()

# print(player.__dict__)