import random
class gue:
    def __init__(self, name):
        self.name = name
        self.money = 10
        self.gladness = 50
        self.alive = True
        
          def work(self):
            self.money += 10
            self.gladness -= 1
            print("я работаю")
        
        def chill(self):
            self.gladness += 1
            self.progress -= 2
            print("я отдохнул")
        
        
        def soping(self):
            self.gladness += 0,5
            self.money -= 1
            print("я пошел в магазин")
            
            
            
              def is_alive(self):
                is self.gladness < 0:
                    print("смерть")
                    self.alive = false
                    elif self.money < 0:
                        print("я голоден")
                        self.alive = false
                      
            
             def info(self):
                                print(f" - {self.gladness}")
                                print(f" - {self.money}")
                                
                                
                                
                                
                                
                                
                                def live(self, day):
     print()
     print(f" ----- день №{day+1}-----")
     print(f"привет, я   {self.name}, и я сегодня:")
     rnd = random.randint(a:1, b:3)
    if rnd == 1:
    self.soping()
    elif rnd  == 2:
        self.work()
        elif rnd == 3:
            self.chill()
            self.is_alive()
     
     
     
     gue = gue("guePetia")
for day in range(365):
if gue.alive == false:
break
gue.life(day)
            
        
            
        
        