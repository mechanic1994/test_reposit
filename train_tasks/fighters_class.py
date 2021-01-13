import random

class Fighter:

    
    def set_names(self, n, n2):
            self.name = n
            self.number = n2
        
        
    def set_health(self, v, d):
            self.values = v
            self.damage = d
    
    
    def get_names(self):
        return self.name
        
        
    def get_health(self):
        return self.values
            
            
first_fighter = Fighter()
second_fighter = Fighter()
first_fighter.set_names('orc', 1)
second_fighter.set_names('hum', 2)
first_fighter.set_health(100, 10)
second_fighter.set_health(100, 10)


while True:


    r = random.randint(1,2)
    if first_fighter.number == r:
        second_fighter.set_health(second_fighter.values - first_fighter.damage, second_fighter.damage)
        print(first_fighter.get_names(), "first_fighter damaged!")
        print(second_fighter.get_names(), "health", second_fighter.get_health())
        if second_fighter.values == 0:
            print('orc win')
            break
        continue
        
        
    elif second_fighter.number == r:
        first_fighter.set_health(first_fighter.values - second_fighter.damage, first_fighter.damage)
        print(second_fighter.get_names(), "second_fighter damaged!")
        print(first_fighter.get_names(), "health", first_fighter.get_health())
        if first_fighter.values == 0:
            print('hum win')
            break
        continue
