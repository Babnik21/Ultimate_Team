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
        if self.firstname != '*':
            return '{ime} {priimek}, {position} from {drzava}, plays for {klub}. Ocena: {rating}'.format(
                ime = self.firstname, priimek = self.lastname, position = self.position, 
                drzava = self.nationality, klub = self.club, rating = self.overall
            )
        else:
            return '{priimek}, {position} from {drzava}, plays for {klub}. Ocena: {rating}'.format(
                priimek = self.lastname, position = self.position, klub = self.club,
                drzava = self.nationality, rating = self.overall
            )

    def __repr__(self):
        if self.firstname == '*':
            return self.lastname
        else:
            return '{0} {1}'.format(self.firstname, self.lastname)