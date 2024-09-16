class Cup:
    def __init__(self, size, quantity):
        self.size = size  
        self.quantity = quantity  
    
    def fill(self, milliliters):
        startus = self.size - self.quantity
        # Nếu có đủ không gian, thêm lượng chất lỏng vào cốc
        if milliliters <= startus:
            self.quantity += milliliters
      
    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)
print(cup.status())  
cup.fill(40)  
cup.fill(20)  
print(cup.status()) 

print("_____________________")

class coc:
    def __init__(self, dungtich, nuoctrongcoc):
        self.dungtich = dungtich
        self.nuoctrongcoc = nuoctrongcoc
    def conlai (self):
        return self.dungtich - self.nuoctrongcoc
    def rot (self, nuoc):
        conlai = self.dungtich - self.nuoctrongcoc
        if nuoc <= conlai:
            self.nuoctrongcoc += nuoc
        
Binh = coc (100,50)
print(Binh.conlai())
print(Binh.rot(20))
print(Binh.rot(50))
print(Binh.conlai())
