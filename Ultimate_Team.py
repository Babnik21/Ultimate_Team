from model import Kartica
import time
import sys

def main_menu():
    print('Kaj želite narediti? Izberite številko pred vašo izbiro:')
    print('1) Išči igralca')
    print('2) Vojna')
    print('3) Sestavi svojo ekipo')
    print('4) Izhod')
    izbira = input('> ')
    if izbira == '4':
        print('Nasvidenje!')
        time.sleep(1)
        sys.exit(0)
    elif izbira == '3':
        pass            #tu bomo dodali funkcijo za igro 'sestavi ekipo'
    elif izbira == '2':
        pass            #tu bomo dodali funkcijo za igro 'Top Trumps'
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

def program():
    intro()
    time.sleep(7)
    while True:
        main_menu()

program()







