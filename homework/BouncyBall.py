class BouncyBall:

    def __init__(self):
        self.air = 10
        self.exploded = False

    def bounce(self):
        if self.exploded:
            print("Sorry, you cannot bounce this ball!  It has exploded.")
        elif self.air <= 3:
            print("Thupp.")
        else:
            print("Bounce!")
            self.air -= 2

    def inflate(self):
        if self.exploded:
            print("Sorry, you cannot inflate this ball!  It has exploded.")
        else:
            self.air += 3
            if self.air > 12:
                print("BANG!!!")
                self.exploded = True

def main():
    b = BouncyBall()

    for i in range(6):
        b.bounce()

    b.inflate()
    b.bounce()
    b.bounce()

    for i in range(5):
        b.inflate()

    b.bounce()

main()
