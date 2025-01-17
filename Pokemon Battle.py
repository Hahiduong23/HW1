class Trainer:
    def __init__(self, name: str):
        self.name = name  
        self.pokemons = []  #danh sách pokemon ban đầu là danh sách rỗng

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"  #trả về thông báo nếu pokemon bắt đã có trong danh sách
        else:
            self.pokemons.append(pokemon)            #thêm pokemon vào danh sách
            return f"Caught {pokemon.pokemon_details()}"  

    def release_pokemon(self, pokemon_name: str):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)               #xoá bỏ pokemon khỏi danh sách nếu khớp
                return f"You have released {pokemon_name}"  
        return "Pokemon is not caught"  
    def trainer_data(self):
        pokemon_details = "\n".join([f"- {pokemon.pokemon_details()}" for pokemon in self.pokemons])
        #tạo chuỗi chi tiết của tất cả các Pokemon trong danh sách

        return (
            f"Pokemon Trainer {self.name}\n"
            f"Pokemon count {len(self.pokemons)}\n"
            f"{pokemon_details}"
        )


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())  
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))  
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))  
print(trainer.add_pokemon(second_pokemon))  
print(trainer.release_pokemon("Pikachu"))  
print(trainer.release_pokemon("Pikachu"))  
print(trainer.trainer_data())  
