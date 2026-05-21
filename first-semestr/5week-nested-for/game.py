import time
import random
import sys


def slow_print(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

slow_print("Hello player.., tell me your name")
player_name = input("My name is ... ")
#Menu = {}

player_stats = {
    "name": player_name,
    "HP": 100,
    "Base ATK": 100,
    "Base DEF": 10,
    "Base SPD": 10,
    "Mana": 0,
    "special skills": 0,
    "level": 0,
    "Exp": 0
}

slime = {
    "name": "Slime",
    "HP": 10,
    "Base ATK": 2,
    "Base DEF": 5,
    "Base SPD": 1,
    "Mana": 0,
    "special skills": 0
}

Boar = {
    "name": "Boar",
    "HP": 35,
    "Base ATK": 5,
    "Base DEF": 8,
    "Base SPD": 12,
    "Mana": 0,
    "special skills": 0
}

Bear = {
    "name": "Bear",
    "HP": 150,
    "Base ATK": 15,
    "Base DEF": 20,
    "Base SPD": 15,
    "Mana": 0,
    "special skills": 0
}
Mosters_exp = {
    "Slime" : 0,
    "Boar" : 0,
    "Bear" : 0
}
def get_exp():
    slime_exp = Mosters_exp["Slime"] * 10
    Boar_exp = Mosters_exp["Boar"] * 50
    Bear_exp = Mosters_exp["Bear"] * 100
    Exp = slime_exp + Boar_exp + Bear_exp
    return Exp

def level_up():
    level = player_stats["level"]
    Exp = player_stats["Exp"]

    if Exp >= (level + 1) * 100:
        slow_print("You can level up!")
        Levelup_consent = input("Do you want to level up? (Y/N): ").upper()
        if Levelup_consent == "Y":
            ask_levelup = input("What do you want to level up? (HP/ATK/DEF/SPD): ").upper()
            if ask_levelup == "HP":
                player_stats["HP"] += 10
            elif ask_levelup == "ATK":
                player_stats["Base ATK"] += 10
            elif ask_levelup == "DEF":
                player_stats["Base DEF"] += 10
            elif ask_levelup == "SPD":
                player_stats["Base SPD"] += 10
            else:
                slow_print("Invalid choice.")
            player_stats["level"] += 1
            slow_print(f"You leveled up! Now you're level {player_stats['level']}.")
            print(player_stats)
        else:
            slow_print("Let's continue then...")
    else:
        slow_print(f"You can't level up yet. You need {(level + 1)*100 - Exp} more EXP.")

slow_print(f"So your name is {player_name}")
check_stats = input("Do you want to check your stats? (Y/N): ")
if check_stats.lower() == "y":
    print(player_stats)
    slow_print("Let's continue ...")
else:
    slow_print("Let's continue ...")


while True:
    consent_battle = input(f"Do you want to test your skills {player_name}? (Y/N): ")
    if consent_battle.lower() == "y":
        slow_print("Let's start the fight then!")
        choose_opponent = input("Choose your opponent (Slime/Boar/Bear): ").lower()
        if choose_opponent == "slime":
            enemy = slime.copy()
        elif choose_opponent == "boar":
            enemy = Boar.copy()
        elif choose_opponent == "bear":
            enemy = Bear.copy()
        else:
            slow_print("Unknown opponent!")
            sys.exit()

        slow_print(f"You are approaching the {enemy['name']}...")
        slow_print("Battle shall start!")

        while player_stats["HP"] > 0 and enemy["HP"] > 0:
            atk_def_consent = input("Do you want to Attack or Defend? (A/D): ").lower()

            if atk_def_consent == "a":
                slow_print("You attack!")
                damage = random.randint(1, player_stats["Base ATK"])
                enemy["HP"] -= damage
                enemy_dmg = random.randint(1, enemy["Base ATK"])
                player_stats["HP"] -= enemy_dmg
                slow_print(f"You dealt {damage} damage. {enemy['name']} HP: {enemy['HP']}")
                #slow_print(f"{enemy['name']} dealt {enemy_dmg} to you, Your HP: {player_stats['HP']} ")


            elif atk_def_consent == "d":
                slow_print("You defend!")
                reduced = random.randint(0, enemy["Base ATK"]) - player_stats["Base DEF"]
                if reduced <= 0:
                    slow_print("You successfully blocked the attack!")
                else:
                    player_stats["HP"] -= reduced
                    slow_print(f"You took {reduced} damage! Your HP: {player_stats['HP']}")
            else:
                slow_print("Invalid choice, you missed your turn!")
            if enemy["HP"] > 0:
                dmg_to_player = max(0, enemy["Base ATK"] - player_stats["Base DEF"] // 2)
                player_stats["HP"] -= dmg_to_player
                slow_print(f"{enemy['name']} attacks and deals {dmg_to_player} damage!")
                slow_print(f"Your HP: {player_stats['HP']} | Enemy HP: {enemy['HP']}")
                print("-" * 30)
        if player_stats["HP"] <= 0:
            slow_print("You have been defeated... Game Over.")
        else:
            Mosters_exp[enemy["name"]] += 1
            slow_print(f"You defeated the {enemy['name']}! You won!")

    else:
        slow_print(f"Then rest well, adventurer {player_name}.")
    print(Mosters_exp)
    player_stats["Exp"] = get_exp()
    print(f"Your total EXP is now {player_stats['Exp']}")
    level_up()
