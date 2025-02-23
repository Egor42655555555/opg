class MyExeption(Exeption):
    def __init__(self, date, line, message):
        self.__date = date
        self.__line = line
        self.__message = message
        
    def save(self):
        f = open("log.txt", 'a', encoding='utf-8')
        f.write(self.__date, + ', line', + self.__line, + ", Message:", + self.__message + "\n")


try:
    a = int(input())
    print(a)
    if a == 0:
        raise MyException( datetime.datetime.now(), line: "18", message: "попытка деления на 0")
        raise ZeroDivisionError("gue")
    print(1/a)
    print(aaa)
except (NameError, ValueError) as err:
    print(err)
    print("name of value error")
except ZeroDivisionError as err:
      print("Zero division error")
      print(err)
except:
    print("fatal error")
    
    
    
    
    
print("code..")




def check_value(var1):
    try:
       if type(var1) != str:
         raise TypeError("var1 not string")
    else:
        return var1
    
        
    
try:
    a = []
    a = check_value(a)
    print(a)
except TypeError as e:
           print(e)