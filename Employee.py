class Employee:
    def __init__(self, emp_id, first_name, last_name, salary):
        self.id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"  
    
    def get_annual_salary(self):
        return self.salary * 12    #tính lương của 12 tháng bằng cách nhân 1 tháng với 12
    
    def raise_salary(self, amount):
        self.salary += amount      #tăng mức lương hiện tại bằng mức lương trước công thêm mức lương tăng quy định 
        return self.salary

employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())      
print(employee.raise_salary(500))    
print(employee.get_annual_salary())  


class Nhanvien:
    def __init__(self, id, ten, ho, luong):
        self.id = id
        self.ten = ten
        self.ho = ho
        self.luong = luong
    
    def tennhanvien(self):
        return f"{self.ho} {self.ten}"
    def luongnam (self):
        return self.luong * 12
    def luongthuong (self,thuong):
        self.thuong = thuong
        self.luong += self.thuong
        return self.luong
trung = Nhanvien (44, "Trung", "Nguyen", 1000)
print(trung.tennhanvien())
print(trung.luongthuong(500))
print(trung.luongnam())
