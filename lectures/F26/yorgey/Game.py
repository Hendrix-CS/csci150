from dataclasses import dataclass
from Pet import *

@dataclass
class Game:

    round: int
    animals: list[Pet]
    d20: Die

    def play(self):
        playing = True
        d20 = Die(20)
        self.animals = []
        while playing:
            print(' '.join(a.animal for a in self.animals))
            r = d20.roll()
            if r < 5:
                print("Nothing happens.")
                input("Hit Enter for the next round.")
            else:
                pet = random_pet(r + self.round)

                print(f'A {pet.display()} appears!')
                keep = input("Would you like to keep it? (y/n) ")
                if keep.lower() == 'y':
                    print('ok!')
                    self.animals.append(pet)
                else:
                    print('no problem')


            self.round += 1


def main():
    game = Game(0, [], None)

    game.play()

main()