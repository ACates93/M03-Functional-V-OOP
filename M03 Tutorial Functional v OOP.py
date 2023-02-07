#################################################
#
# M03 Tutorial Functional V OOP 
#
# Allene Cates
#
# 02/06/2023
#
# This program takes a list of patients at a vet clinic 
# and prints them for the user to see
##################################################

class Pet():
    # Initialize the properties
    def __init__(self, petType, name, age, gender, breed, vaccinated, note):
        self.petType = petType
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        self.vaccinated = vaccinated
        self.note = note

# Inherit from the Pet Class
class Dog(Pet):
    def __init__(self,petType, name, age, gender, breed, vaccinated, houseBroken, aggressive, obedience, note):
        super().__init__(petType, name, age, gender, breed, vaccinated, note)
        self.houseBroken = houseBroken
        self.aggressive = aggressive
        self.obedience = obedience

    # Prints dog details
    def show_details(self):
        print("Type:", self.petType)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Breed:", self.breed)
        print("Vaccinated:", self.vaccinated)
        print("House Broken:", self.houseBroken)
        print("Aggressive:", self.aggressive)
        print("Obedience Training:", self.obedience)
        print("Notes:", self.note)



class Cat(Pet):
    def __init__(self, petType, name, age, gender, breed, vaccinated, litterBox, declawed, note):
        super().__init__(petType, name, age, gender, breed, vaccinated, note)
        self.litterBox = litterBox
        self.declawed = declawed

    # Prints cat details
    def show_details(self):
        print("Type:", self.petType)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Breed:", self.breed)
        print("Vaccinated:", self.vaccinated)
        print("Litter Box Trained:", self.litterBox)
        print("Declawed:", self.declawed)
        print("Notes:", self.note)


dog = Dog('Dog', 'Jax', '4yrs', 'Male', 'Boxer', 'Yes', 'Yes', 'No', 'Intermediete', 'Jax has a history of eating things he should not. Please keep this in mind if he comes in with stomach issues.\n')
dog1 = Dog('Dog', 'Freya', '2yrs', 'Female', 'Great Dane', 'Yes', 'Yes', 'No', 'Beginner', 'Freya has anxiety and must take trazedone before coming into the office.\n       Please have owners pick up script the day before\n')
dog2 = Dog('Dog', 'Ben', '9yrs', 'Male', 'Boxer', 'Yes', 'Yes', 'Yes', 'Master', 'Ben is a loving dog but is also dog agressive.\n       They will have to wait in the car if we have other patients in the lobby.\n')
cat = Cat('Cat', 'Mischa', '7yrs', 'Female', 'Bombay', 'No', 'Yes', 'Yes', 'Mischa is a very sweet cat. She was found on the side of the road and is now being fostered through the animal shelter.\n')
cat1 = Cat('Cat', 'Frank', '6mo', 'Male', 'Tabby', 'Yes', 'Yes', 'No', 'Frank is a young patient and we do not know much about him. Please add more notes as needed.\n')
cat2 = Cat('Cat', 'Felix', '5yrs', 'Male', 'Sphynx', 'Yes', 'Yes', 'Yes', 'Felix is blind in both eyes and has an owner that cares greatly for him.\n')


dog.show_details()
dog1.show_details()
dog2.show_details()
cat.show_details()
cat1.show_details()
cat2.show_details()