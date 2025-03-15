class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50 
        self.energy = 50  

    def feed(self):
        self.hunger = max(0, self.hunger - 10)
        print(f"{self.name} покушал! Голод: {self.hunger}/100")

    def sleep(self):
        self.energy = 100
        print(f"{self.name} отдохнул! Энергия: {self.energy}/100")

    def __str__(self):
        return f"{self.species} {self.name} (Голод: {self.hunger}, Энергия: {self.energy})"


class PetStore:
    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)
        print(f"{pet.name} добавлен в зоомагазин!")

    def sell_pet(self, name):
        for pet in self.pets:
            if pet.name == name:
                self.pets.remove(pet)
                print(f"{pet.name} продан!")
                return pet
        print(f"Питомец {name} не найден!")
        return None

    def list_pets(self):
        if not self.pets:
            print("В зоомагазине нет питомцев!")
        else:
            for pet in self.pets:
                print(pet)



store = PetStore()

pet1 = Pet("Пушок", "Котик")
pet2 = Pet("Макс", "Собака")

store.add_pet(pet1)
store.add_pet(pet2)

store.list_pets()  

sold_pet = store.sell_pet("Макс")  
if sold_pet:
    sold_pet.feed()  
store.list_pets()  
