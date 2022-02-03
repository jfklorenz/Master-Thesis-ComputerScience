import random

class huenchen:
    
    def __init__(self, name, rundheit):
        self.name = name
        self.rundheit = rundheit
        self.official = True
        print(self.name)
        self.identify()
        self.rund()
        
        print(' ')
        
    def identify(self):
        if self.name == 'Pupshühnchen':
            print('Pups!!!')
        elif self.name == 'Trollhühnchen':
            print('hihihi')
        else:
            self.official = False
            
        if self.official == True:
            print("Official Hühnchen R")
        else:
            print("Neues Hühnchen, yay!")

    def rund(self):
        if self.rundheit > 5:
            print("Schön rund!")
        else:
            print("Nicht rund genug!")
    
    def bok(self):
        
        r = random.random()
        
        if r < 0.25:
            print('Bok')
        elif r < 0.5:
            print('Bgok')
        elif r < 0.75:
            print('Bokbok')
        elif r < 0.8:
            print('Bök')
        elif r < 0.85:
            print('BOOOOOK')
        elif r < 0.9:
            print('bok hihi')
        elif r < 0.95:
            print('zzzZZZzzzbokzzz')
        else:
            print('yaaaaaaaaay')
    
    
#H1 = huenchen('Trollhühnchen', 3)
#H2 = huenchen('Kochhühnchen', 8)

Hx = huenchen('Mysteriöses Hühnchen', 6)

for i in range(20):
    Hx.bok()