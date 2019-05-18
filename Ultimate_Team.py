from model import Kartica
import time
import sys
from random import randint, choice

def main_menu():
    print('Kaj želite narediti? Izberite številko pred vašo izbiro:')
    print('1) Navodila')
    print('2) Išči igralca')
    print('3) Vojna')
    print('4) Sestavi svojo ekipo')
    print('5) Izhod')
    izbira = input('> ')
    if izbira == '5':
        print('Nasvidenje!')
        time.sleep(1)
        sys.exit(0)
    elif izbira == '4':
        pass            #tu bomo dodali funkcijo za igro 'sestavi ekipo' (mogoče)
    elif izbira == '3':
        Top_Trumps()    #Verzija 1.0
    elif izbira == '2':
        browser()       #Verzija 1.0       
    elif izbira == '1':
        pass            #Dodamo 2 txt fila za navodila za top trumps in sestavi ekipo
    else:
        print('Vpisali ste neveljaven znak. Poskusite ponovno.')
        time.sleep(1)

def intro():                            #Izpiše uvodno besedilo
    with open('Besedila\intro.txt', 'r', encoding = 'utf-8') as intro:
        tekst = intro.read()
        print(tekst)

#Dobimo seznam igralcev iz premier lige
with open("Lige\Premier_Liga.txt", 'r', encoding = 'utf-8') as data:
    seznam_igralcev = []
    for vrstica in data:
        if vrstica[0] == '*':
            continue
        seznamcek = vrstica.strip().split(', ')
        seznam_igralcev.append(Kartica(seznamcek))

def TT_dolzina():                       #Uporabnika vpraša po želeni dolžini igre, vrne število kartic
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

def TT_razdeli():                       #Na začetku igre razdeli karte
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

def get_hand(player_list):              #izbere naključnega igralca iz seznama
    return choice(player_list)

def vprasaj_po_kljucu(igralec):         #Vrne indeks lastnosti igralca
    if igralec.position == 'GK':
        print('Izberite kategorijo:')
        print('1) Diving: {0}'.format(igralec.attributes[0]))
        print('2) Handling: {0}'.format(igralec.attributes[1]))
        print('3) Kicking: {0}'.format(igralec.attributes[2]))
        print('4) Reflexes: {0}'.format(igralec.attributes[3]))
        print('5) Speed: {0}'.format(igralec.attributes[4]))
        print('6) Positioning: {0}'.format(igralec.attributes[5]))
        izbira = input('> ')
        if izbira not in '123456' or izbira == '':
            print('Neveljavna izbira!')
            return vprasaj_po_kljucu(igralec)
        else:
            return int(izbira) - 1
    else:
        print('Izberite kategorijo:')
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

def get_key(user, na_potezi):           #Vpraša uporabnika po ključu ali vrne naključnega
    if na_potezi == True:
        return vprasaj_po_kljucu(user)
    else:
        return randint(0, 5)

def boljši_v_kategoriji(prvi, drugi, kljuc):    #ugotovi, ali je prvi premagal drugega
    if prvi.attributes[kljuc] > drugi.attributes[kljuc]:
        return True
    else:
        return False

def predstavi_igralca(igralec):         #Uporabniku predstavi igralca na voljo
    if igralec.firstname != '*':
        print('Igralec na voljo je {0} {1}, {2}, {3}'.format(
            igralec.firstname, igralec.lastname, igralec.club, igralec.nationality))
    else:
        print('Igralec na voljo je {0}, {1}, {2}'.format(igralec.lastname,
        igralec.club, igralec.nationality))
    if igralec.position == 'GK':
        print('Vaš igralec je vratar.')

def obvesti_kdo_izbira(napotezi):       #Obvesti uporabnika, kdo izbira
    if napotezi:
        print('Na potezi ste, da izberete kategorijo.')
        time.sleep(1)
    else:
        print('Nasprotnik je na potezi, da izbere kategorijo.')
        time.sleep(2)

def zaključek_tt(user_p):               #Uporabniku sporoči razplet igre
    if len(user_p) == 0:
        print('Izgubili ste. Več sreče Prihodnjič!')
    else:
        print('Čestitke! Zmagali ste!')
    time.sleep(1)


def Top_Trumps():                       #Igra top trumps
    igralci = TT_razdeli()
    user_players = igralci[:(len(igralci)//2)]
    ai_players = igralci[(len(igralci)//2):]
    na_potezi = True
    while len(user_players) != 0 and len(ai_players) != 0:
        user = get_hand(user_players)
        ai = get_hand(ai_players)
        predstavi_igralca(user)
        time.sleep(0.5)
        obvesti_kdo_izbira(na_potezi)
        kljuc = get_key(user, na_potezi)
        if boljši_v_kategoriji(user, ai, kljuc):
            print('Zmagali ste! Dobili ste novega igralca!')
            ai_players.remove(ai)
            user_players.append(ai)
            na_potezi = True
        elif boljši_v_kategoriji(ai, user, kljuc):
            print('Izgubili ste, vašega igralca je dobil nasprotnik.')
            user_players.remove(user)
            ai_players.append(user)
            na_potezi = False
        else:
            print('Izenačeno! Oba obdržita svojega igralca.')
    zaključek_tt(user_players)


def ustreza_poizvedbi(keyword, item):   #preveri, ali igralec ustreza poizvedbi
    if len(keyword) == 0:
        return True
    elif keyword[-1] == '*':
        if len(keyword[:-1]) > len(item):
            return False
        else:
            for prva, druga in zip(keyword[:-1], item):
                if prva != druga:
                    return False
            return True
    else:
        return keyword == item

def isci_po_seznamu(poskus, kljuc, seznam):     #Funkcija vrne seznam igralcev, ki ustrezajo poizvedbi
    resitev = []
    for el in seznam:
        if ustreza_poizvedbi(poskus, el.seznam_podatkov()[kljuc]):
            resitev.append(el)
    return resitev

def pridobi_kljuc_za_iskanje():         #Vrne ključ, po katerem bomo iskali igralce
    print('Izberite, po katerem podatku želite poiskati igralca:')
    time.sleep(0.5)
    print('1) Priimek (Ime)')
    print('2) Pozicija')
    print('3) Državljanstvo')
    print('4) Klub')
    print('5) Vrni se v začetni meni')
    izbira = input('> ')
    if izbira == None or izbira not in '12345':
        time.sleep(0.5)
        print('Neveljavna izbira!')
        time.sleep(0.5)
        return pridobi_kljuc_za_iskanje()
    else:
        if izbira == '5':
            return 100
        else:
            return int(izbira) - 1

def pridobi_keyword():                  #Funkcija vrne keyword po katerem iščemo
    print('Vnesite podatek o iskanem igralcu:')
    podatek = input('> ')
    if podatek == None:
        time.sleep(0.5)
        print('Neveljaven podatek!')
        time.sleep(0.5)
        return pridobi_keyword()
    return podatek

def nadaljuj_iskanje():                 #Vrne true če uporabnik želi iskati le med pravkar najdenimi igralci
    print('Ali želite nadaljevati z iskanjem po izpisanem seznamu igralcev?')
    time.sleep(0.5)
    print('1) Da')
    print('2) Ne')
    odgovor = input('> ')
    if odgovor == '1':
        return True
    elif odgovor == '2':
        return False
    else:
        time.sleep(0.5)
        print('Neveljaven odgovor.')
        time.sleep(0.5)
        return nadaljuj_iskanje()

def izhod_iz_brskalnika():
    print('Želite nadaljevati z iskanjem ali se želite vrniti v začetni meni?')
    time.sleep(0.5)
    print('1) Nadaljuj z iskanjem')
    print('2) Vrni se v začetni meni')
    odgovor = input('> ')
    if odgovor == '1':
        return False
    elif odgovor == '2':
        return True
    else:
        print('Neveljaven odgovor.')
        time.sleep(0.5)
        return izhod_iz_brskalnika()


def browser():                          #Brskalnik za iskanje igralcev iz seznama
    nadaljuj = False
    while True:
        if not nadaljuj:
            seznam = seznam_igralcev
        key = pridobi_kljuc_za_iskanje()
        if key > 50:
            break
        keyword = pridobi_keyword()
        seznam = isci_po_seznamu(keyword, key, seznam)
        for el in seznam:
            print(el)
            time.sleep(0.5)
        if len(seznam) == 0:
            print('Vašemu iskanju ne ustreza noben igralec v bazi!')
        nadaljuj = nadaljuj_iskanje()
        if not nadaljuj:
            seznam = seznam_igralcev
            if izhod_iz_brskalnika():
                time.sleep(0.5)
                break


def program():
    intro()
    time.sleep(3)           #spremeni na 7
    while True:
        main_menu()

program()







