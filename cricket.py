class Player:
    def play(self):
        print("the player is playing cricket")

class Batman(Player):
    def play(self):
        print("the batsman is batting.")

class Bowler(Player):
    def play(self):
        print("the bowler is bowling.")

bat=Batman()
bat.play()

bow=Bowler()
bow.play()