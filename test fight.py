import random

from Hero import Hero

hero1 = Hero("Ion", 100, 15, 75, 24)
hero2 = Hero("Vasile", 51, 0, 32, 67)


def lineStage(main, enemy):
    chanceGetPowerMain = main.last_hit / (main.last_hit + enemy.denay)
    chanceGetPowerEnemy = enemy.last_hit / (enemy.last_hit + main.denay)
    for i in range(0, 10):
        main.setPower(main.power + getPower(chanceGetPowerMain))
        enemy.setPower(enemy.power + getPower(chanceGetPowerEnemy))
    return [main, enemy]


def getPower(chance_of_one):
    random_value = random.random()

    if random_value < chance_of_one:
        return random.randint(5, 10)
    else:
        return 0


heroPower = lineStage(hero1, hero2)
print("Power Main: ", heroPower[0])
print("Power Enemy: ", heroPower[1])