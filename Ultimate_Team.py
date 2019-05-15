from model import Kartica
import time
import sys
from random import randint, choice

def main_menu():
    print('Kaj želite narediti? Izberite številko pred vašo izbiro:')
    print('1) Išči igralca')
    print('2) Navodila')
    print('3) Vojna')
    print('4) Sestavi svojo ekipo')
    print('5) Izhod')
    izbira = input('> ')
    if izbira == '5':
        print('Nasvidenje!')
        time.sleep(1)
        sys.exit(0)
    elif izbira == '4':
        pass            #tu bomo dodali funkcijo za igro 'sestavi ekipo'
    elif izbira == '3':
        pass
        Top_Trumps()    #Nedokončana
    elif izbira == '2':
        pass            #Dodamo 2 txt fila za navodila za top trumps in sestavi ekipo
    elif izbira == '1':
        pass            #tu dodamo search engine za iskanje igralcev
    else:
        print('Vpisali ste neveljaven znak. Poskusite ponovno.')

def intro():
    with open('Besedila\intro.txt', 'r', encoding = 'utf-8') as intro:
        tekst = intro.read()
        print(tekst)

with open("Lige\Premier_Liga.txt", 'r', encoding = 'utf-8') as data:
    seznam_igralcev = []
    for vrstica in data:
        if vrstica[0] == '*':
            continue
        seznamcek = vrstica.strip().split(', ')
        seznam_igralcev.append(Kartica(seznamcek))

def TT_dolzina():
    print('Število kartic, ki jih dobi igralec, vpliva na trajanje igre.')
    print('Izberite dolžino igre:')
    print('1) Kratka (5 kartic na igralca)')
    print('2) Srednje dolga (10 kartic na igralca)')
    print('3) Dolga (20 kartic na igralca)')
    print('4) Nazaj')
    izbira = input('> ')
    if izbira == '1':
        return 10
    elif izbira == '2':
        return 20
    elif izbira == '3':
        return 40
    elif izbira == '4':
        return -1
    else:
        print('Vnesli ste neveljaven znak. Poskusite ponovno.')
        return 0

def TT_razdeli():
    dolzina = 0
    players_zacasno = []
    while dolzina == 0:
        dolzina = TT_dolzina()
    if dolzina == -1:
        return [1]
    for _ in range(dolzina):
        a = randint(0, len(seznam_igralcev) - 1)
        players_zacasno.append(seznam_igralcev[a])
    return players_zacasno

def get_hand(player_list):
    return choice(player_list)

def vprasaj_po_kljucu(igralec):         #vrne indeks lastnosti igralca
    if igralec.position == 'GK':
        print('Izberite kategorijo:')
        print('1) Diving: {0}'.format(igralec.attributes[0]))
        print('2) Handling: {0}'.format(igralec.attributes[1]))
        print('3) Kicking: {0}'.format(igralec.attributes[2]))
        print('4) Reflexes: {0}'.format(igralec.attributes[3]))
        print('5) Speed: {0}'.format(igralec.attributes[4]))
        print('6) Positioning: {0}'.format(igralec.attributes[5]))
        izbira = input('> ')
        if izbira not in '123456':
            print('Neveljavna izbira!')
            return vprasaj_po_kljucu(igralec)
        else:
            return int(izbira) - 1
    else:
        print('Izberite kategorijo:'
        print('1) Pace: {0}'.format(igralec.attributes[0]))
        print('2) Shooting: {0}'.format(igralec.attributes[1]))
        print('3) Passing: {0}'.format(igralec.attributes[2]))
        print('4) Dribbling: {0}'.format(igralec.attributes[3]))
        print('5) Defending: {0}'.format(igralec.attributes[4]))
        print('6) Physical: {0}'.format(igralec.attributes[5]))
        izbira = input('> ')
        if izbira not in '123456':
            print('Neveljavna izbira!')
            return vprasaj_po_kljucu(igralec)
        else:
            return int(izbira) - 1

def get_key(user, na_potezi):       #vpraša userja po ključu ali vrne naključnega
    if na_potezi == True:
        return vprasaj_po_kljucu(user)
    else:
        return randint(0, 5)

def Top_Trumps():
    igralci = TT_razdeli()
    user_players = igralci[:(len(igralci)//2)]
    ai_players = igralci[(len(igralci)//2):]
    na_potezi = True
    while len(user_players) != 0 and len(ai_players) != 0:
        pass

def program():
    intro()
    time.sleep(2)           #spremeni na 7
    while True:
        main_menu()

program()







