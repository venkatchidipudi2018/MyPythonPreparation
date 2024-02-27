class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2024 - birth_year
        return cls(name, age)

    @staticmethod
    def is_adult(age):
        return age >= 18

# Create an instance of the Person class
person = Person("Alice", 25)

# Call an instance method
person.talk()

# Call a class method
person = Person.from_birth_year("Alice", 1999)

# Call a static method
print(Person.is_adult(25))
