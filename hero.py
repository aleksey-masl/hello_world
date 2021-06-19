class Hero():
    '''Class to create Hero for our game'''
    def __init__(self, name, level, race):
        '''Initiate our Hero'''
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        '''Print all parameters of this Hero'''
        discription = (self.name+ " Level is:"+ str(self.level) + " Race is: " + self.race + " Health is " + str(self.health)).title()
        print(discription)

    def level_up(self):
        '''Upgrade level of Hero'''
        self.level += 1

    def move(self):
        '''Start moving Hero'''
        print("Hero " + self.name + " start moving...")

    def set_health(self, new_health):
        self.health = new_health

class SuperHero(Hero):
    '''Class to create SuperHero'''
    def __init__(self, name,level, race, magiclevel):
        '''Initiate our SuperHero'''
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.magic = 100

    def makemagic(self):
        '''Using magic'''
        self.magic -= 10

    def show_hero(self):
        '''Print all parameters of this Hero'''
        discription = (self.name+ " Level is:"+ str(self.level) + " Race is: " + self.race +
                       " Health is " + str(self.health) + " Magic is: " + str(self.magic)).title()
        print(discription)