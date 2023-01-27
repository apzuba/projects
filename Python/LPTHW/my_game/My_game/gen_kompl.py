from imie_script import imie_1


#The compliment generator module
class Komplement():

    def kompl():

        from random import randint

        Obiekt_komplementu_meski = ['Uśmiech', 'Intelekt', 'Wygląd', 'Zapach', 'Głos',
        'Całokształt', 'Humor', 'Wzrok', 'Mięsień', 'Charakter']

        Obiekt_komplementu_meski = ((' '.join(Obiekt_komplementu_meski)).lower()).split()

        Czasownik = ['wygląda', 'prezentuje się', 'pociąga', 'podoba się',
        'zachwyca', 'urozmaica', 'uzmysławia', 'ogarnia']
        Przymiotnik = ['niesamowicie', 'przenikająco', 'cudownie', 'przemiło', 'przenosząco',
        'rozkochiwująco', 'angażująco', 'doprowadzająco', 'onieśmielająco', 'opętająco', 'rozgrzewająco']
        Porownanie = ['jak', 'niczym', 'tak jak', 'zupłenie jak', 'przypominając']
        Rzeczownik_komplementu = ['miłość', 'marzenie', 'przejemność', 'raj na ziemii',
        'najszczęśliwszy moment mojego życia', 'Bradd Pitt', 'wakacje pod palmami', 'urok', 'szczęście', 'Angelina Jolie']

        komplement = []

        def start_komplement():
            imie = imie_1
            if imie == '':
                imie = 'Drogi anonimie'
            else:
                pass

        # #generator losowych słów
        #     ob_kompl_meski = Obiekt_komplementu_meski.pop(random.randint(0,len(Obiekt_komplementu_meski)-1))
        #     czas = Czasownik.pop(random.randint(0,len(Czasownik)-1))
        #     przym = Przymiotnik.pop(random.randint(0,len(Przymiotnik)-1))
        #     porow = Porownanie.pop(random.randint(0,len(Porownanie)-1))
        #     rzecz_komp = Rzeczownik_komplementu.pop(random.randint(0,len(Rzeczownik_komplementu)-1))

        #personalisation for the sex of the player
            if imie[-1] == 'a':
                imie = imie[0:len(imie) - 1] + 'o'

                #print compliment female function
                def druk_k():

                    ob_kompl_meski = Obiekt_komplementu_meski.pop(randint(0,len(Obiekt_komplementu_meski)-1))
                    Obiekt_komplementu_meski.append(ob_kompl_meski)

                    czas = Czasownik.pop(randint(0,len(Czasownik)-1))
                    Czasownik.append(czas)

                    przym = Przymiotnik.pop(randint(0,len(Przymiotnik)-1))
                    Przymiotnik.append(przym)

                    porow = Porownanie.pop(randint(0,len(Porownanie)-1))
                    Porownanie.append(porow)

                    rzecz_komp = Rzeczownik_komplementu.pop(randint(0,len(Rzeczownik_komplementu)-1))
                    Rzeczownik_komplementu.append(rzecz_komp)

                    print(f" \nDroga {imie}, Twój {ob_kompl_meski} {czas} \n{przym} {porow} {rzecz_komp}. \n \t\t\t --Dla Ciebie, Adam")

                    
                    #get more compliments
                    powrtorka = input("Czy chcesz jeszcze raz? (t/n) >")

                    if powrtorka == 'n':
                        exit(0)

                    else:
                        druk_k()

                druk_k()

            else:
                #print compliment male function
                def druk_m():

                    ob_kompl_meski = Obiekt_komplementu_meski.pop(randint(0,len(Obiekt_komplementu_meski)-1))
                    Obiekt_komplementu_meski.append(ob_kompl_meski)

                    czas = Czasownik.pop(randint(0,len(Czasownik)-1))
                    Czasownik.append(czas)

                    przym = Przymiotnik.pop(randint(0,len(Przymiotnik)-1))
                    Przymiotnik.append(przym)

                    porow = Porownanie.pop(randint(0,len(Porownanie)-1))
                    Porownanie.append(porow)

                    rzecz_komp = Rzeczownik_komplementu.pop(randint(0,len(Rzeczownik_komplementu)-1))
                    Rzeczownik_komplementu.append(rzecz_komp)

                    print(f" \n{imie}, Twój {ob_kompl_meski} {czas} \n{przym} {porow} {rzecz_komp}. \n \t\t\t --Dla Ciebie, Adam")

                    powrtorka = input("Jeszcze jeden komplement? :) (t/n) >")

                    if powrtorka == 'n':
                        play_again = input("Chcesz zagrać jeszcze raz? (Y/N) >\t")

                        if play_again == "Y" or play_again == "y":

                            Start.gogo()

                        else:
                            exit(0)

                    else:
                        druk_m()

                druk_m()

        start_komplement()
