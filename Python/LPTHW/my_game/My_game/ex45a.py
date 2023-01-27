#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

from random import randint
from textwrap import dedent

import gen_kompl
import imie_script

from ex45_combat import Combat
import ex45_combat
from ex45_death import Death

import ex45_game_stats
from ex45_game_stats import game_stats



class Game():
    pass

class Engine():

#This essentially runs the script, imports the script name and runs the selected gogo() method
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('the-end')

        while current_scene != last_scene:
            current_scene = \
            self.scene_map.next_scene(current_scene.gogo())

        current_scene.gogo()

#Scenarios classess
class WejscieSmoka(Game):

    #gogo() function starts the scenario
    def gogo(self):

        for i in dedent(f"""
                    ---PROLOG---
                    {imie_script.imie_1}, witaj w Galaktycznych Zombie-Ninjach 1.0.
                    Zostałeś wysłany/a na statek kosmiczny Hokomoto II z misją zbadania pojawienia się
                    na nim nieokreślonych kreatur, które opanowały statek.
                    Jako Mokatyn klasy-6Z8 nie raz brałeś udział w niebezpiecznych misjach tego typu.
                    Odkryj w jaki sposób pokonać jak największą liczbę obcych i oczywiście, przeżyj.
                    Powodzenia 6Z8-{imie_script.imie_1}!
                    """):
                sys.stdout.write(i)
                time.sleep(0.04)
        for i in dedent(f"""
                    ---PIERWSZE SPOTKANIE---
                    ...Przypominasz sobie, że czytałeś że każdy obcy posiada tylko jeden słaby punkt.
                    Oprócz pieniędzy oczywiście. Za kilkadziesiąt UKL każdy potwór zostawi cię w spokoju.
                    Ty obecnie masz {ex45_game_stats.game_stats.pocket_money} UKL przy sobie.
                    Ponoć pistolet i katana działają na więcej niż jednego potwora...
                    ...
                    Chodzisz typowym dla Mokatynów twojej klasy, bezszelestnym chodem.
                    Jesteś na korytarzu głównym, gdzie słyszysz hałasy. To twoje pierwsze spotkanie z obcymi.
                    """):
                sys.stdout.write(i)
                time.sleep(0.04)
                
        #Combat.attack() loads the fight module
        Combat.attack()
        for i in dedent(f"""
            Wow. Co za pierwsze napotkanie...
            Potrzebuję uważnie obserwować jak mogę walczyć z tymi kreaturami...
            Ugh. Zauważasz że Twój kombinezon został uszkodzony... Przez to będziesz mógł przetrwać jeden atak mniej.
            """):
            sys.stdout.write(i)
            time.sleep(0.04)
            
        #returns the next scenario
        return 'shoguniada'


class Shoguniada(Game):

    def gogo(self):
        
        #changes the HP points setting
        ex45_game_stats.game_stats.defence = 2

        for i in dedent(f"""
            ---WYŁUDZACZ---
            Przemierzasz statek kosmiczny swoim niezawodnym Mokato-chodem i docierasz do sekcji B.

            W oddali widzisz zakrytą postać, która podchodzi w twoim kierunku. Nie jesteś pewien czy jest groźna.
            """):
            sys.stdout.write(i)
            time.sleep(0.04)
        cwaniak = input("'Czy jest tu jakiś cwaniak??' - pyta przenikliwym głosem.\n > [tak] [nie] ? ")
        if cwaniak == "nie" or cwaniak == "n":
            time.sleep(0.04)
            print("To daj pieniążka.")

        elif cwaniak == "tak" or cwaniak == "t":
            print("'uhuhuhu. No to zobaczymy!' (postać używa jakiegoś rodzaju magii...)")
            Combat.attack()
            for i in dedent(f"'Pokonałeś mojego przywołaka, ale teraz będzie cię to kosztowało.'"):
                sys.stdout.write(i)
                time.sleep(0.04)

        else:
            time.sleep(0.04)
            print("Nie rozumiem. Daj pieniążka.")

        #The money handling scene (UKL is the currency of the game).
        prosti_money = input(f"""
        \rMasz {ex45_game_stats.game_stats.pocket_money} UKL w kieszeni.
        Ile pieniędzy chcesz przekazać nieznanej postaci? >
        """)
        while prosti_money.isnumeric() == False:
            prosti_money = input("Wpisz proszę liczbę! Ile pieniędzy chcesz przekazać? \n> ")

        def money_exchange(a):
            prosti_money_12 = ""
            for i in range(len(prosti_money)):
                for b in range(10):
                    if a[i] == str(b):
                        prosti_money_12 += a[i]
                    else:
                        pass
            return prosti_money_12

        prosti_money_12 = int(money_exchange(prosti_money))
        print(f"'Dam ci {prosti_money} UKL.'")
        time.sleep(0.04)
        print("'Niech pomyślę ile to będzie w systemie binarnym...''")
        time.sleep(0.10)
        current_money = ex45_game_stats.game_stats.pocket_money - prosti_money_12

        if prosti_money_12 <= ex45_game_stats.game_stats.pocket_money and prosti_money_12 > 30:
            time.sleep(0.04)
            for i in dedent(f"""
                        "Dobrze, tyle mi starczy.""
                        Zakryta postać bierze twoje UKLe i pozwala ci pójść dalej.
                        """):
                sys.stdout.write(i)
                time.sleep(0.04)
            return 'autostrada'


        elif prosti_money_12 > game_stats.pocket_money:
            for i in (f"""  Oszust! Ty nie masz tyle UKLów! """):
                sys.stdout.write(i)
                time.sleep(0.04)
            Combat.attack()
            if ex45_game_stats.game_stats.hard_damage == True:
                print("W trakcie walki uszkodzona została twoja powłoka elektryczna. [Punkty Życia = 2]")
                ex45_game_stats.game_stats.defence = 1
            else:
                pass
            return 'autostrada'

        else:
            for i in (f"Hmm... tylko tyle?? MUAHAHAHA. GIŃ!"):
                sys.stdout.write(i)
                time.sleep(0.04)
            Combat.attack()
            if ex45_game_stats.game_stats.hard_damage == True:
                print("W trakcie walki uszkodzona została twoja powłoka elektryczna. [Punkty Życia = 2]")
                ex45_game_stats.game_stats.defence = 1
            else:
                pass
            return 'autostrada'


class Autostrada(Game):

    def gogo(self):

        opcje_autostrada =['stacja', 'armorownia', 'kuchnia']

        for i in dedent(f"""
            ---NASTĘPNY KIERUNEK---
            Spisujesz w notatkach raportowych swoje ostatnie napotkanie.
            Zastanawiasz się, czy powinieneś kontynuować misję.
            Otocznie jest bardziej niebezpiecznie niż podejrzewałeś.\n
            Widzisz trzy opcje na wyjście z obecnej sytuacji.
            1) Pójdź do stacji komunikacyjnej. Wezwiesz posiłki od Komisariusza UrsusZB5.
            2) Pójdź do armorowni po kombinezon ochronny. On istotnie zwiększy twoje zdolności obronne.
            3) Zgłodniałeś. A tylko jedną przecznicę dalej jest kuchnia, z pyszną Pizzą Kosmolitańską... Mmmm.
            """):
            sys.stdout.write(i)
            time.sleep(0.04)

        autos = True
        while autos == True:

            print(opcje_autostrada)
            wybor_autostrada = input("Gdzie idziesz? > ")

            if wybor_autostrada == "stacja":
                print("""
                Biegniesz do stacji. Na szczęście w drodze nie napotkałeś nikogo ani niczego groźnego.
                Otwierasz drzwi oddziału komunikacyjnego...""")
                Combat.attack()
                print("Te pomieszczenie zdaje się być pełne tych groźnych stworzeń!")
                Combat.attack()
                if ex45_game_stats.game_stats.hard_damage == True:
                    print("W trakcie walki uszkodzona została twoja powłoka elektryczna. [Punkty Życia = 2]")
                    ex45_game_stats.game_stats.defence = 1
                else:
                    pass

                for i in dedent(f"""
                    Przyjście tutaj to nie był dobry pomysł! Uciekasz.
                    Potrzebujesz lepszej ochrony. Decydujesz skierować się do armorowni.
                    ...
                    Przechodząc zauważasz wyrytą na ścianie liczbę '-11' i wyraźne ślady walki.
                    Ciekawe czy to coś znaczy.
                    """):
                    sys.stdout.write(i)
                    time.sleep(0.04)
                autos = False
                return 'przygoda_rzycia'

            elif wybor_autostrada == "armorownia":
                for i in dedent(f"""
                    Tak, lepsza ochrona to dobry pomysł.
                    Znasz standardowe rozmieszczenie armorowni w statkach tego typu.
                    Nagle, przechodząc obok dziwnie zniekształconych, ale wciąż zamkniętych drzwi,
                    padasz na kolana i łapiesz się za głowę...
                    """):
                    sys.stdout.write(i)
                    time.sleep(0.04)
                for i in dedent(f"""
                    "Będziesz słuuuużył. Będziesz mi słuuuużył."
                    -słyszysz głos w swojej głowie.
                    To musi być czarno-nindżyjska magia...
                    "Zrobisz co ci każęęęę!!!"
                    Z każdym słowem odczuwasz coraz mniej kontroli nad sobą.
                    Jednak dobrze pamiętasz skuteczne obrony przed magią umysłu.
                    Matematyka. Musisz szybko rozwiązać jakieś matematyczne równanie.
                    """):
                    sys.stdout.write(i)
                    time.sleep(0.04)
                rownianie_2 = input("Ile to jest:  23 + 2 * 3 - 4 * 2 / 0.2  ? > ")
                if rownianie_2 == "-11":

                    print("Dobrze. Udało ci się oswobodzić z magii umysłu potwora.")
                    time.sleep(0.04)
                    print("Ciekawe czy ta liczba coś znaczy..")
                    autos = False
                    return 'przygoda_rzycia'

                else:
                    print("Spróbuj jeszcze raz...")

                    rownianie_2 = input("Ile to jest:  23 + 2 * 3 - 4 * 2 / 0.2  ? > ")
                    if rownianie_2 == "-11":
                        print("Dobrze. Udało ci się oswobodzić z magii umysłu potwora.")
                        time.sleep(0.04)
                        print("Ciekawe czy ta liczba coś znaczy..")
                        autos = False
                        return 'przygoda_rzycia'

                    else:
                        print("Nie.. to nie tak.. W trakcie twojego myślenia zostałeś zaatakowany.")
                        Combat.attack()
                        if ex45_game_stats.game_stats.hard_damage == True:
                            print("W trakcie walki uszkodzona została twoja powłoka elektryczna. [Punkty Życia = 2]")
                            ex45_game_stats.game_stats.defence = 1
                        else:
                            pass
                        print("Potwór pokonany, ale czujesz że to ostatnia szansa by uwolnić się od opętającej magii umysłu..")

                        rownanie = input("(-4 - x)^2 -20 = 5 \n  Ile wynosi x? > ")
                        if rownanie == ("-11"):

                            print("Dobrze. Udało ci się oswobodzić!")
                            time.sleep(0.04)
                            print("Ciekawe czy to tylko przypadkowa liczba..")
                            autos = False
                            return 'przygoda_rzycia'
                        else:
                            Combat.attack()
                            print("""
                            W trakcie walk, tajemnicza moc opanowała kontrolę nad twoim umysłem
                            Stałeś się jednym ze sługów czarnej ninja-magii.
                            """)
                            Death.gogo()
            elif wybor_autostrada == "kuchnia":
                for i in dedent(f"""
                    "Zawsze jest czas na zdrową i pyszną pickę. Od razu czujesz się lepiej.
                    Przypominasz sobie, że celem twojej misji jest zdobycie jak największej
                    liczby informacji na temat kreatur. Potwory zdają się być groźne.
                    "Potrzebuję lepszej ochrony. To pozwoli mi dużo bezpieczniej zbadać efektywne metody walki."
                    Teraz, najedzony i szczęśliwy, decydujesz się skierować do armorowni po kombinezon ochrony.
                    """):
                    sys.stdout.write(i)
                    time.sleep(0.04)
                autos = False
                for i in dedent(f"""
                    Przechodząc zauważasz wyrytą na ścianie liczbę '-11' i wyraźne ślady walki.
                    Ciekawe czy to coś znaczy.
                    """):
                    sys.stdout.write(i)
                    time.sleep(0.04)
                return 'przygoda_rzycia'
            else:
                pass



class Przygoda(Game):

    def gogo(self):
        for i in dedent(f"""
            ---ARMOROWNIA---
            Droga minęła spokojnie. Dochodzisz do drzwi armorowni.
            Drzwi są wgniecione, i masz podejrzenie że system elektroniczny został zmodyfikowany.
            """):
            sys.stdout.write(i)
            time.sleep(0.04)

        kod_poprawny = False
        proba_drzwi = 0
        while kod_poprawny == False:
            kod_drzwi = input("\nWpisz kod drzwi> ")
            if kod_drzwi == "-1011":
                for i in dedent(f"""
                    Sukces. Drzwi otwierają się. W środku znajdujesz kombinezon ochronny i zakładasz go.
                    Od teraz będziesz w stanie wytrzymać dodatkowy atak każdego przeciwnika.
                    [Punkty Życia = 3])
                    """):
                    sys.stdout.write(i)
                    time.sleep(0.04)
                ex45_game_stats.game_stats.defence = 2
                kod_poprawny = True

                for i in dedent(f"""
                    ---WYPEŁNIĆ MISJĘ---
                    Z nowym kombinezonem czujesz się bezpieczniej. To pora by wykonać misję do końca.
                    Potrzebujesz przekazać Komisariuszowi UrsusZB5 to co dowiedziałeś się do tej pory.
                    Pora by wybrać się do stacji komunikacyjnej.
                    ...
                    Docierasz do sekcji komunikacyjnej statku kosmicznego.
                    Widzisz, że wewnątrz znajduje się kilku nieumarłych ninja lub innych potworów.
                    Po drugiej stronie znajdują się drzwi do byłej sekcji zaopatrzeniowej. Być może znajdziesz tam coś przydatnego.
                    """):
                    sys.stdout.write(i)
                    time.sleep(0.04)
                choice_kapsula = False
                while choice_kapsula == False:
                    wybor_kapsula = input("[komunik], [zaopatrz]\nGdzie chcesz wejść? > ")
                    if wybor_kapsula == "komunik" or wybor_kapsula == "kom%":
                        choice_kapsula = True
                        return 'kapsula'
                    elif wybor_kapsula == "zaopatrz" or wybor_kapsula == "zao%":
                        choice_kapsula = True
                        return 'zaopatrz'
                    else:
                        print("Nie rozumiem. Wpisz swój wybór poprawnie.")

            elif kod_drzwi != "-1011" and proba_drzwi <2:
                print("Hmm. Kod nie działa. Wyłudzacz pieniędzy wspominał coś o kodzie binarnym... ")
                proba_drzwi += 1
            else:
                print("Hmm. Kod nie działa. Kosmici chyba się zorientowali że próbujesz się tutaj dostać.")
                Combat.attack()
                if ex45_game_stats.game_stats.hard_damage == True:
                    print("W trakcie walki uszkodzona została twoja powłoka elektryczna. [Punkty Życia = 2]")
                    ex45_game_stats.game_stats.defence = 1
                else:
                    pass
                print("\nTa liczba którą wcześniej napotkałem.. Chyba powinienem wpisać ją w formie binarnej...")
                proba_drzwi += 1


class Kapsula(Game):

    def gogo(self):
        for i in dedent(f"""
            ---STACJA KOMUNIKACYJNA---
            Nie jesteś tutaj sam. To czas by pokonać kilu obcych!
            """):
            sys.stdout.write(i)
            time.sleep(0.04)
        Combat.attack()
        print("Pierwszy obcy z głowy. Ahh, nadchodzi kolejny.")
        Combat.attack()
        print("Jeszcze jeden!")
        Combat.attack()
        for i in dedent(f"""
            Udało ci się pokonać wszystkich w stacji! To czas połączyć się z Komisariuszem UrsusZB5.
            ...
            bip bip bip. --connecting-- --connecting-- --connected--
            "Halo, 6Z8-{imie_script.imie_1}, zdaj raport z misji."
            """):
            sys.stdout.write(i)
            time.sleep(0.04)
        raport = input("(tu wpisz swój raport) > ")
        for i in dedent(f"""
            "Rozumiem 6Z8-{imie_script.imie_1}. Dobra robota."
            """):
            sys.stdout.write(i)
            time.sleep(0.04)

        #Mid-mission raporting
        raport_liczba = "a"
        while raport_liczba.isnumeric() == False:
            raport_liczba = input("Ile słabych punktów obcych udało ci się rozpracować? > ")
        raport_liczba_int = int(raport_liczba)

        if raport_liczba_int > 8 or raport_liczba_int < 0:
            for i in dedent(f"""
                "6Z8-{imie_script.imie_1}, coś kręcisz. Nie rozpoznaliśmy tylu typów obcych.
                [W strefie zaopatrzeniowej powinieneś znaleźć dodatkowy elektrostymulator ochronny.
                Przyda ci się dla lepszej ochrony.]
                [Możesz także iść na poszukiwanie potworów. Tylko w ten sposób dowiesz\r
                się jakie słabości mają ich kolejne gatunki.]
                Wróć do mnie gdy rozpracujesz słabe punkty przynajmniej pięciu typów obcych."
                """):
                sys.stdout.write(i)
                time.sleep(0.04)
            wybor_kom_true = True
            while wybor_kom_true == True:
                print("[zaopatrz], [poszukiwanie]")
                wybor_kom = input("Co chcesz zrobić? > ")
                if wybor_kom == "zaopatrz":
                    wybor_kom_true = False
                    return 'zaopatrz'
                elif wybor_kom == "poszukiwanie":
                    wybor_kom_true = False
                    return 'poszukiwanie'
                else:
                    print("Nie rozumiem. Proszę wpisz poprawnie.")
        elif raport_liczba_int < 5:
            for i in dedent(f"""
                "6Z8-{imie_script.imie_1}, to jeszcze za mało by wypełnić misję.
                [W strefie zaopatrzeniowej powinieneś znaleźć dodatkowy elektrostymulator ochronny.
                Przyda ci się dla lepszej ochrony.]
                [Możesz także iść na poszukiwanie potworów. Tylko w ten sposób dowiesz\r
                się jakie słabości mają ich kolejne gatunki.]
                Wróć do mnie gdy rozpracujesz słabe punkty przynajmniej pięciu typów obcych."
                """):
                sys.stdout.write(i)
                time.sleep(0.04)
            wybor_kom_true = True
            while wybor_kom_true == True:
                print("[zaopatrz], [poszukiwanie]")
                wybor_kom = input("Co chcesz zrobić? > ")
                if wybor_kom == "zaopatrz":
                    wybor_kom_true = False
                    return 'zaopatrz'
                elif wybor_kom == "poszukiwanie":
                    wybor_kom_true = False
                    return 'poszukiwanie'
                else:
                    print("Nie rozumiem. Proszę wpisz poprawnie.")
        else:
            for i in dedent(f"""
                "Świetnie 6Z8-{imie_script.imie_1}, tylu obcych nam wystarczy."
                """):
                sys.stdout.write(i)
                time.sleep(0.04)
            return 'raport'

#The supplies-shop
class Zaopatrz(Game):

    def gogo(self):
        for i in dedent(f"""
            ---STREFA ZAOPATRZENIOWA---
            W strefie zaopatrzeniowej możesz uzupełnić swoje zapasy ochronne.
            System wymaga jednak opłaty. Kompletny pancerz [Punkty Życia: 4] kosztuje 70 UKL.
            [Posiadasz {ex45_game_stats.game_stats.pocket_money} UKL].
            Kup pancerz, wróć do Stacji Komunikacyjnej (uwaga, obcy mogą być w stacji),
            lub wyrusz na poszukiwania obcych po statku.
            """):
            sys.stdout.write(i)
            time.sleep(0.04)

        wybor_zaopatrz_true = True
        while wybor_zaopatrz_true == True:
            print("[kup_ochrone], [komunik], [poszukiwanie]")
            wybor_zaopatrz = input("Co chcesz zrobić? > ")

            #Buying the HP protection element
            if wybor_zaopatrz == "kup_ochrone" and ex45_game_stats.game_stats.pocket_money > 69:
                ex45_game_stats.game_stats.defence = 3
                ex45_game_stats.game_stats.pocket_money -= 70
                for i in dedent(f"""
                    Świetnie. Zyskałeś maksymalną ochronę. [Punkty Życia: 4]
                    Pozostało ci: {ex45_game_stats.game_stats.pocket_money} UKL.
                    """):
                    sys.stdout.write(i)
                    time.sleep(0.04)

            elif wybor_zaopatrz == "kup_ochrone" and ex45_game_stats.game_stats.pocket_money <= 69:
                print("Nie masz wystarczająco dużo pieniędzy.")

            elif wybor_zaopatrz == "komunik":
                wybor_zaopatrz_true = False
                return 'kapsula'

            elif wybor_zaopatrz == "poszukiwanie":
                wybor_zaopatrz_true = False
                return 'poszukiwanie'

            else:
                print("Wpisz proszę poprawnie.")

#Spaceship exploration
class Poszukiwanie(Game):

    def gogo(self):
        for i in dedent(f"""
            ---POSZUKIWANIE---
            Eksplorujesz statek kosmiczny Hokomoto II w celu znalezienia nowych przeciwników.
            Pamiętasz, że jesteś tutaj po to by odkryć słabości obcych.
            W oddali słyszysz jakiś hałas... Tak, to twój przeciwnik.
            """):
            sys.stdout.write(i)
            time.sleep(0.04)
        Combat.attack()
        posz_true = True
        while posz_true == True:
            print("Dobra robota. Walka wygrana. Chcesz eksplorować dalej?")
            posz_dalej = input("[t / tak] [n / nie]? > ")
            if posz_dalej == "n" or posz_dalej == "nie":
                print("Chcesz iść do Strefy Zaopatrzeniowej, czy zdać raport w Stacji Komunikacyjnej? ")
                posz_wybor = input("[kup_ochrone], [komunik]? > ")
                if posz_wybor == "kup_ochrone":
                    posz_true = False
                    return 'zaopatrz'
                elif posz_wybor == 'komunik':
                    posz_true = False
                    return 'komunik'
                else:
                    print("Zdecyduj się.")
            elif posz_dalej == "t" or posz_dalej == "tak":
                print("Poszukujesz kolejnego obcego. Znalezienie go nie było trudne!")
                Combat.attack()
            else:
                print("Wpisz poprawnie.")

#End-of-the-game report mission
class Raport(Game):

    def gogo(self):

        print(f"Nasi funkcjonariusze zidentyfikowali obecne na Hokomoto II typy obcych.")
        raport_done = False
        raport = {}
        raport_dobry_obcy = []
        l_obcy_raport = 0

        while raport_done == False:
            print(f"\nOto lista potworów które możesz zraportować:\n{Combat.shoguns_list}  lub  [wyjdz]")
            current_obcy = input("Wpisz nazwę obcego do zraportowania. > ")

            # TYPE THE MONSTERN
            if current_obcy in Combat.shoguns_list:

                #TYPE THE WEAKNESS
                print(f'Ok. Jaką słabość ma {current_obcy}?\n\nTwoje znane rodzaje ataków: {Combat.attacks[0:6]}.')
                current_obcy_weakness = input("> ")

                if current_obcy_weakness in Combat.attacks[0:6]:

                    Combat.shoguns_list.remove(current_obcy)

                    #CHECKS IF THEY GOT THE RAPORT WEAKNESS RIGHT
                    raport[current_obcy] = current_obcy_weakness
                    if raport[current_obcy] == Combat.shoguns_base[current_obcy]:
                        raport_dobry_obcy.append(current_obcy)
                    else:
                        pass

                    #Checks if there are enough elements in report to submit it
                    l_obcy_raport += 1
                    print(f"\nL. obcych w raporcie: {l_obcy_raport}.\nTwój obecny raport: {raport}")
                    if l_obcy_raport > 4:
                        raport_is_done = input(f"""
                        Spisałeś raport nt.{l_obcy_raport} obcych. To powinno wystaczyć.
                        Przesłać raport?  [tak] [nie] >
                        """)
                        if raport_is_done == "tak" or raport_is_done == "t":
                            print("... Przesyłam raport Komisariuszowi UrsusZB5...")
                            raport_done = True

                            #Checks if the report is correct
                            if len(raport_dobry_obcy) == l_obcy_raport:
                                #report correct, you win
                                return 'the-end'
                            else:
                                #report is wrong, redirects to exploring the spaceship scenario
                                Combat.shoguns_list = ['Shoghun-ghul', 'Ronin', 'Ninja', 'Unspecified-Undead',
                                                'Space-assasin', 'Zombie', 'Uzaki-Monk', 'Undead-deity']
                                for i in dedent(f"""
                                    "6Z8-{imie_script.imie_1}, z naszych sprawdzownych danych wywiadowczych wynika że w twoim raporcie
                                    znajduje się przynajmniej jeden błąd. Wróć zdać raport gdy będziesz pewny że jest poprawny."\n
                                    Decydujesz się wyruszyć w poszukiwania po statku by zebrać więcej danych na temat potworów.
                                    """):
                                    sys.stdout.write(i)
                                    time.sleep(0.04)
                                raport_done = True
                                return 'poszukiwanie'

                        else:
                            pass
                    else:
                        pass
                else:
                    print('\nWpisz nazwę ataku poprawnie.')
            elif current_obcy == "wyjdz":
                raport_done = True
                return 'poszukiwanie'

            elif current_obcy == 'q':
                exit(0)

            else:
                print('\nWpisz nazwę potwora poprawnie.')


#The end
class Ending(Game):

    def gogo(self):
        print(f"6Z8-{imie_script.imie_1}, świetna robota. \n------- ZWYCIĘSTWO! HIP HIP HURAH. :) -------\n")
        
        #redirects to the winners gift - a compliments generator!
        gen_kompl.Komplement.kompl()

#The maps loader - this class manages the maps loading and the game engine
class Map():

    def __init__(self, start_scene):
        self.start_scene = start_scene

    scenarios = {
                'wejscie_smoka': WejscieSmoka(),
                'shoguniada': Shoguniada(),
                'autostrada': Autostrada(),
                'przygoda_rzycia': Przygoda(),
                'kapsula': Kapsula(),
                'zaopatrz': Zaopatrz(),
                'poszukiwanie': Poszukiwanie(),
                'raport': Raport(),
                'death': Death(),
                'the-end': Ending()
            }
    #loads the following scene
    def next_scene(self, scene_name):
        loading = Map.scenarios.get(scene_name)
        return loading

    #loads the first scene
    def opening_scene(self):
        return self.next_scene(self.start_scene)

# current_scenario = self.play_map.opening_scene()
# last_scenario = self.play_map.loading_scene('the-end')
#
# while current_scenario is not last_scenario:
#     current_scenario = self.play_map.loading_scene(current_scenario.gogo())

class Start():
    def gogo():
        Engine(Map('wejscie_smoka')).play()

if __name__ == "__main__":
    Start.gogo()
