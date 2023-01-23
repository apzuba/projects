"""This is module for the Game Combat"""

from random import randint
from textwrap import dedent

import time
import sys

from ex45_death import Death
import ex45_game_stats
from ex45_game_stats import game_stats


class Combat():

#HEALTH POINTS ITEMS UPDATING FUNCTION
    def attack():
        if ex45_game_stats.game_stats.defence == 2:
            Combat().shogun_attack(2)
        elif ex45_game_stats.game_stats.defence == 1:
            Combat().shogun_attack(1)
        elif ex45_game_stats.game_stats.defence == 3:
            Combat().shogun_attack(3)
        else:
            print("--- coś poszło nie tak---")



    attacks = ['magic-spell', 'laser-katana', 'laser-pistol', 'pee', 'smile', 'scream', '30 UKL']

    shoguns_list = ['Shoghun-ghul', 'Ronin', 'Ninja', 'Unspecified-Undead',
                    'Space-assasin', 'Zombie', 'Uzaki-Monk', 'Undead-deity']

    shoguns_base = {
                    'Shoghun-ghul': 'laser-pistol',
                    'Ronin': 'laser-katana',
                    'Ninja': 'laser-pistol',
                    'Unspecified-Undead': 'magic-spell',
                    'Space-assasin': 'laser-pistol',
                    'Zombie': 'laser-katana',
                    'Uzaki-Monk': 'scream',
                    'Undead-deity': 'pee'
                    }

# FIGHT MODULE
    def shogun_attack(self, armor):
        self.armor = armor

        shoguns_type = Combat.shoguns_list[randint(0,7)]

        if self.armor == 1:
            health_points = 1
        elif self.armor == 2:
            health_points = 2
        elif self.armor == 3:
            health_points = 3
        else:
            pass


        for i in dedent(f"""
                Napotkałeś na {shoguns_type}.
                [ Punkty życia: {health_points + 1} ]  |  To twoje opcje ataku to:
                {Combat.attacks}
                """):
            sys.stdout.write(i)
            time.sleep(0.03)

        while True:
            attack = input("Co robisz? > ")

            Not_effective = [
                            f"Uh, {attack} nie było zbyt efektywne...",
                            f"{attack} - nie zadziałało...",
                            f"Na tego przeciwnika potrzebujesz zrobić coś innego niż {attack}"
                            ]

            att_not_eff = Not_effective.pop(randint(0,len(Not_effective)-1))
            Not_effective.append(att_not_eff)

            Effective = [
                            f"Tak, {attack} zadziałało świetnie!",
                            f"Rozwaliło {shoguns_type} na strzępy!",
                            f"Yakamatatuza! {shoguns_type} został kompletnie rozwalony przez {attack}."
                            ]
            att_eff = Effective.pop(randint(0,len(Effective)-1))
            Effective.append(att_eff)

            if attack == Combat.shoguns_base.get(shoguns_type):

                for i in dedent(f"""
                        {att_eff}
                        """):
                    sys.stdout.write(i)
                    time.sleep(0.02)

                hard_damage = False
                gold = randint(3,12)
                ex45_game_stats.game_stats.pocket_money = ex45_game_stats.game_stats.pocket_money + gold
                print(f"Znalazłeś przy potworze {gold} UKL. Masz teraz {ex45_game_stats.game_stats.pocket_money} UKL.")
                return False

            elif attack == "quit" or attack == "q":
                exit(0)

            elif attack == "30UKL" or attack == "30" or attack == "30 UKL" or attack == "30 ukl":
                if ex45_game_stats.game_stats.pocket_money > 30:

                    for i in dedent(f"""
                            Obcy są bardzo łakomi na pieniądze. 30 UKL kupuje ci wolność.
                            """):
                        sys.stdout.write(i)
                        time.sleep(0.02)

                    ex45_game_stats.game_stats.pocket_money -= 30
                    ex45_game_stats.game_stats.hard_damage = False
                    return False
                else:
                    print("Nie masz tyle pieniędzy.")


            elif attack != Combat.shoguns_base.get(shoguns_type)\
                and health_points != 0:
                health_points -= 1

                wrong_text = dedent(f"""
                            {att_not_eff}
                            {shoguns_type} zaatakował cię!
                            Oberwało ci się, ale będziesz jeszcze w stanie spróbować zaatakować ponownie.
                            WALCZ O PRZETRWANIE!! [ Punkty życia: {health_points + 1} ]
                            """)
                for i in wrong_text:
                    sys.stdout.write(i)
                    time.sleep(0.02)

                if health_points == 1:
                    ex45_game_stats.game_stats.hard_damage = True
                else:
                    pass

            else:
                print(f"\nSHokomotota! {shoguns_type} zabija cię. :<\n")
                Death.gogo()
