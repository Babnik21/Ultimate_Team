
## Zaenkrat prazna datoteka, tu bo naš program

class Kartica:
    def __init__(self, sez):
        self.lastname = sez[0]
        self.firstname = sez[1]
        self.position = sez[2]
        self.nationality = sez[3]
        self.club = sez[4]
        self.overall = int(sez[5])
        self.attributes = [int(x) for x in sez[6:]]
    
    def In_Form(self):
        seznam = []
        for el in self.attributes:
            el += 5
            seznam.append(el)
        self.attributes = seznam


