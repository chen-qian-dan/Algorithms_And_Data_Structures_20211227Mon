"""
Q5_Animal Shelter
An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. 
People must adopt either the "oldest" (based on arrived time) of all animals at the shelter, 
or they can select whether they would prefer a dog or a cat (can will receive the oldest animal of that type). 
They cannot select which specific animal they would like. 
Create the data structures to maintain this system and implement operations such as 
enqueue, dequeueAny, dequeueDog, and dequeueCat. 
"""
from typing import List 

class Animal:
    def __init__(self, name: str, type: str):
        self.name: str = name 
        self.type: str = type 

class AnimalShelter:
    def __init__(self):
        self.queue: List[Animal] = list()
        self.stack: List[Animal] = list()

    def enqueue(self, name: str, type: str):
        self.queue.append(Animal(name = name, type = type))

    def dequeueAny(self):
        if len(self.queue) == 0:
            return "The shelter is empty"
        return self.queue.pop(0)

    def _dequeueType(self, type: str):
        if len(self.queue) == 0:
            return "The shelter is empty"

        retAnimal = None 
        while len(self.queue) > 0:
            animal = self.queue.pop(0)
            if animal.type == type:
                retAnimal = animal
                break 
            else:
                self.stack.append(animal)
        while len(self.stack) > 0:
            a = self.stack.pop()
            self.queue.insert(0, a)
        
        if not retAnimal:
            return "There is not such type of animal"
        return retAnimal

    def dequeueDog(self):
        return self._dequeueType(type = "Dog")
    
    def dequeueCat(self):
        return self._dequeueType(type = "Cat")



animalShelter = AnimalShelter()
animalShelter.enqueue('1', type = "Dog")
animalShelter.enqueue('2', type = "Dog")
animalShelter.enqueue('3', type = "Cat")
a = animalShelter.dequeueCat()
if type(a) == Animal:
    print(a.name)
else:
    print(a)
