class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1

    @classmethod
    def show_player_count(cls):
        return cls.player_count
    
p1 = Player("Raj",1)
p2 = Player("Surya",2)
p3 = Player("ABD",1)

print(Player.show_player_count())