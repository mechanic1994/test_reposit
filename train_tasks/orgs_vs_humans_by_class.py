import time, random


list_human = []
list_orc = []
count = 0


class Fighters:
    unique_number = 0
    def __init__(self):
        self.race = random.randint(1, 2)
        Fighters.unique_number += 1
        self.number = Fighters.unique_number


class Hero(Fighters):
    lvl = 0
    def __init__(self, r):
        Fighters.__init__(self)
        self.race = r
    def lvl_up(self):
        self.lvl += 1
        return self.lvl


class Solders(Fighters):
    def go_behind(self, h):
        if h == hero_human:
            army_human = len(list_human)
            random_human = (random.randint(1, army_human)) - 1
            pick_human = list_human[random_human]
            print ("Человек с номером ", pick_human.number,\
                   "Следует за героем людей с номером ", hero_human.number)
        elif h == hero_orc:
            army_orc =len(list_orc)
            random_orc = (random.randint(1, army_orc)) - 1
            pick_orc = list_orc[random_orc]
            print ("Орк с номером ", pick_orc.number,\
                   "Следует за героем орков с номером ", hero_orc.number)
        else:
            pass


hero_human = Hero(1)
hero_orc = Hero(2)


while True:
    count = 0
    while count < 20:
        new_solder = Solders()
        if new_solder.race == 1:
            list_human.append(new_solder)
            count += 1
        else:
            list_orc.append(new_solder)
            count +=1


    order = new_solder.go_behind(hero_human)
    order_2 = new_solder.go_behind(hero_orc)
    order_3 = new_solder.go_behind(4)
    time_out = time.sleep(5)


    if len(list_human) > len(list_orc):
        hero_human.lvl_up()
        print ("Уровень героя у людей", hero_human.lvl)
        list_human.clear()
        list_orc.clear()
        if hero_human.lvl == 5:
            print ("Люди победили")
            break
        else:
            continue
    elif len(list_orc) > len(list_human):
        hero_orc.lvl_up()
        print ("Уровень героя у орков", hero_orc.lvl)
        list_human.clear()
        list_orc.clear()
        if hero_orc.lvl == 5:
            print ("Орки победили")
            break
        else:
            continue
    else:
        hero_human.lvl_up()
        hero_orc.lvl_up()
        print ("Герой людей", hero_human.lvl, "Герой орков", hero_orc.lvl)
        list_human.clear()
        list_orc.clear()
        if hero_human.lvl == 5 or hero_orc.lvl == 5:
            print ("Ничья")
            break
        else:
            continue
