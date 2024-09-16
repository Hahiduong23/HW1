class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items
    
    def get_items_count(self):
        return len(self.items)   #trả về lượng phần tử trong danh sách


my_shop = Shop("SuperMart", ["Apples", "Bananas", "Cucumbers"])
print(my_shop.get_items_count())

