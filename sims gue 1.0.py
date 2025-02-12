import time
import random
import threading
class Human:
    def __init__(self, name, house, car=None, job=None):
        self.name = name
        self.house = house
        self.car = car
        self.job = job
        self.money = 1000
        self.gladness = 50
        
        def shopinggue(self):
            if self.car == none:
                print("идем в магазин пешком")
                else:
                    self.car.drive(random.randint(a:10, b:40))
                    self.money -= random.randint(a: 5, b:15)
                    self.house.food += random.randint(a:5, b:20)
        
        def shoping(self):
            def __init__(self, grocery, building):
                self.grocery = grocery
                self.building = building
                
                
            def grocery(self, grocery):
                def random_numer(1, 2):
                    return random.randint(1, 2)
                random _num = random_number(1, 2)
                
                if random_numer = 1
                self.money -= 20
                self.food += 10
                print("вы сходили в маленький магазин")
                
                elif:
                    self.money -= 50
                    self.food += 40
                    self.fuel -= 10
                    print("вы приехали в гипермаркет")
                    
                    
                    if self.fuel < 10:
                        print("поездка невозможна")
                    
                    
                    
                    class Building:
                        def __init__(self, store)
                        self.store = store
                        self.running = False
                        self.thread = None
                        
                        def run_periodically(self, interval):
                            if not self.running:
                                self.running = True
                                self.Thread = threading.Thread(target = self._loop, args=(interval,), daemon = True)
                                self.thread.start()
                                
                                
                                def _loop(self, interval):
                                    while self.running:
                                        self.action()
                                        time.sleep(interval)
                                        
                                        def stop(self):
                                            self.running = False
                                            
                                            
                                            input("нажмите Enter, чтобы запустить...\n")
                                            my_building.run_periodically(3)
                                            
                                            input("нажмите Enter, чтобы остановить...\n")
                                            my_building.stop()
                                            
                                            #тут я попробовал написать функицию для того чтобы нельзя было спамить ремонтом дома
                                            
                                            
                                            def building(self, store)
                                            self.healt += 20
                                            self.money -= 50
                                            self.fuel -= 20
                                            
                                            if self.fuel < 20:
                                                print("поездка невозможна")
                        
        
        def work(self):
            self.money += random.randint(a: 40, b: 50)
            self.money += salary
            print("сегодня работаем. заработали {salary}")
        
        def eat(self):
            self.gladness += 5
            food = random.randint(a:1, b:5)
            self.house.food - food > 0:
                self.house.food -= food
                print("мы чуть чуть поели")
                else:
                    print("поесть не удалось, холодильник пустой")
        
        def chill(self):
           print("сегодня отдыхаем")
           self.money -= random.randint(a:5, b:10)
           self.house.pollution += random.randint(a:1, b:5)
           self.gladness += random.randint(a:5, b:10)
        
        def cleaning(self):
           percent = random.randint(a:1, b:5)
           if percent == 5:
               print("сегодня генеральная уборка")
               self.house.pollution = 0
               else:
                   print("сегодня только повытирали пыль")
                   self.house.pollution = max(0, self.house.pollution - random.randint(a:1, b:3))
        
        def info(self):
            print(f"деньги {self.money}")
            print(f"настроение {self.gladness")
                    
        
        def live(self):
            print(f"--- день№{day}---")
            self.work()
            self.eat()
            self.chill()
            self.shoping()
            if day % 5 == 0:
                self.cleaning()
                
                
                
                self.info()
                
            
        
        def is_alive(self):
            if self.money < 0:
                return False
            return True
        
        
        class car:
            def __init__(self, model):
                self.model = model
                self.fuel = 60
                self.state = 100
                
                def drive(self, length):
                    rashod = length * 0.1
                    if self.fuel - rashod < 0:
                        print("надо идти пешком")
                        else:
                            self.fuel -= rashod
                            self.state -= lenght * 0.01
                            print(f"мы поехали {length} км, потратили {rashod} л топлива")
                            
                            if self.money < 6000:
                                self.car = false
                                self.fuel = false
                                self.state = false
                                elif:
                                    self.money > 6000:
                                        self.money -= 5000
                                        self.car = true
                                        self.fuel = true
                                        self.state = true
                                        
                
                def add_fuel(self, fuel):
                    if self.fuel + fuel <= 60:
                        self.fuel += fuel
                        print(f"мы заправили {fuel} л бензина")
                        else:
                            self.fuel = 60
                            print("бак полный")
                
                def __str__(self):
                    return f"машина{self.model},топливо{self.fuel}л,износ{self.state}"
        
        
        
        class Job:
            def __init__(self, name, salary):
                self.name = name
                self.salary = salary
                
                
                def __str__(self):
                    return f"робота: {self.name},  зарплата - {self.salary}"
                
                
                class House:
                    def __init__(self):
                        self.pollution = 0
                        self.food = 0
                        self.healt = 100
                        def countdown(start):
                            while start > 0:
                                print(start)
                                time.sleep(100)
                                self.healt -= 5
                                
                                else:
                        
                        def __str__(self):
                            return(f"запас еды - {self.food}, стпень загрязнения {self.pollution}")
                            
                            
                            
                            
                            
                            
                            human = human(name:"gue", job=Job(name:"cварщик", salary: 1000), house=House())
                            for day in range(1, 365):
                                if human.is_alive() == False:
                                    break
                                    human.live(day)
