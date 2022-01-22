import re
from Cattest1 import Cat

cat_1 = Cat('Baron', 'boy', 2)
cat_2 = Cat('Sam', 'boy', 2)

print(f'First cat: {cat_1.name}, its a {cat_1.sex}, age of {cat_1.age}')
print(f'First cat: {cat_2.name}, its a {cat_2.sex}, age of {cat_2.age}')


class Dog(Cat):
    def get_pet(self):
        return f'{self.get_name()}, {self.get_age()}'

dog_1 = Dog('Felix', 'boy', 3)

print(dog_1.get_pet())