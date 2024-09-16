class Flower:
    def __init__(self, name, water_requirements):      
    
        self.name = name  
        self.water_requirements = water_requirements  
        self.is_happy = False                   #tình trạng của hoa ban đầu mặc định là ko vui
    
    def water(self, quantity):
    
        if quantity >= self.water_requirements: #nếu lượng nước tưới là lớn hơn hoặc bằng lượng nước cần thiết thì trả về kq happy là true
            self.is_happy = True
    
    def status(self):
        if self.is_happy:                       #kiểm tra và trả về kết qủa của cây vui hay là ko vui với lượng nước tưới thêm 
            return f"{self.name} is happy"
        else:
            return f"{self.name} is not happy"



flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())  
flower.water(60)
print(flower.status())  
flower.water(100)
print(flower.status())  

class Hoa:
    def __init__(self, ten , bu):
        self.ten = ten
        self.bu = bu
        self.hanhphuc = False
    def nuoc (self, luong):
        if luong >= self.bu:
            self.hanhphuc = True
    def trangthai(self):
        if self.hanhphuc:
            return f"{self.ten} hanh phuc"
        else:
            return f"{self.ten} ko hanh phuc"
        
Hong = Hoa("Trung", 100)
Hong.nuoc(20)
print(Hong.trangthai())
Hong.nuoc(100)
print(Hong.trangthai())
        


