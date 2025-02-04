import random
class gue:
    def __init__(self, name):
        self.name = name
        self.progress = 10
        self.gladness = 50
        self.alive = True
        
        
        def study(self):
            self.progress += 0,1
            self.gladness -= 1
            print("я учусь")
        
        def chill(self):
            self.gladness += 1
            self.progress -= 2
            print("я отдохнул")
        
        
        def sleep(self):
            self.gladness += 0,5
            print("я пошел спать")
            
            
            
            def is_alive(self):
                is self.gladness < 0:
                    print("смерть")
                    self.alive = false
                    elif self.progress < 0:
                        print("пусто в голове")
                        self.alive = false
                        elif self.progress > 50:
                            print("я закончил академию шаг")
                            self.alive = false
                            
                            
                            def info(self):
                                print(f" - {self.gladness}")
                                print(f" - {self.progress}")
                                
 
 def live(self, day):
     print()
     print(f" ----- день №{day+1}-----")
     print(f"привет, я   {self.name}, и я сегодня:")
     rnd = random.randint(a:1, b:3)
    if rnd == 1:
    self.study()
    elif rnd  == 2:
        self.sleep()
        elif rnd == 3:
            self.chill()
            self.is_alive()
     
     
                                
gue = gue("guePetia")
for day in range(365):
if gue.alive == false:
break
gue.life(day)
            
        
        
        
        