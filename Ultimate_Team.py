class Kartica:     #kartica bo predstavljala posameznega igralca
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

    def __str__(self):
        return '{ime} {priimek}, {position} from {drzava}, currently plays for {klub}, rating: {rating}'.format(
            ime = self.firstname, priimek = self.lastname, position = self.position, 
            drzava = self.nationality, klub = self.club, rating = self.overall
        )


with open("Premier_Liga.txt", 'r', encoding = 'utf-8') as data:
    seznam_igralcev = []
    for vrstica in data:
        if vrstica[0] == '*':
            continue
        seznamcek = vrstica.strip().split(', ')
        seznam_igralcev.append(Kartica(seznamcek))

print(seznam_igralcev[0])







