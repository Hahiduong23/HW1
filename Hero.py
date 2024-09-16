class Hero:
    def __init__(self, name ,health):
        self.name = name
        self.health = health
    def defend(self,damage):
        self.health -= damage   #lượng máu sẽ giảm bằng số sát thương nhận vào
        if self.health <= 0:   
            self.health = 0     #đảm bảo cho lượng máu là ko âm
            return f"{self.name} was defeated"     #máu bằng 0 thì nhân vật chết 
    
    def heal(self, amount):    
        self.health += amount   #lương máu sẽ tăng bằng số máu hồi 
        return f"{amount}"
hero = Hero("Peter", 100)
print(hero.defend(50))  
print(hero.heal(50))
print(hero.defend(99))  
print(hero.defend(1))   

class Anhhung:
    def __init__(self, ten, mau):
        self.ten = ten 
        self.mau = mau
    def andam (self,dam):
        self.mau -= dam
        if self.mau < 1:
            self.mau = 0
            return f"{self.ten} đã chết"
    def hoimau (self, hoi):
        self.mau += hoi
        if self.mau >100:
            self.mau = 100
            return f"{self.ten} đã hồi full máu"
anhhung1 = Anhhung("trung",100)
print(anhhung1.andam(20))
print(anhhung1.hoimau(50))
print(anhhung1.andam(100))
        

