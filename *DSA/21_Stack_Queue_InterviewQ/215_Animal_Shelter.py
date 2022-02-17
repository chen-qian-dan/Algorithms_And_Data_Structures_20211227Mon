"""
Q5_Animal Shelter
An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. 
People must adopt either the "oldest" (based on arrived time) of all animals at the shelter, 
or they can select whether they would prefer a dog or a cat (can will receive the oldest animal of that type). 
They cannot select which specific animal they would like. 
Create the data structures to maintain this system and implement operations such as 
enqueue, dequeueAny, dequeueDog, and dequeueCat. 
"""

# use a queue and stack to implement it
from collections import deque 

class Animal:
    def __init__(self, name: str, type: str):
        self.name = name 
        self.type = type 

class AnimalShelter:
    def __init__(self):
        self.queue = deque()
        self.stack = deque() 

    def __str__(self):
        return str([(v.name, v.type) for v in self.queue])


    def enqueue(self, name: str, type: str):
        animal: Animal = Animal(name, type)
        self.queue.append(animal)

    def _dequeueType(self, type: str):
        if len(self.queue) == 0:
            return None 
        ret = None 
        while len(self.queue) > 0:
            animal = self.queue.popleft()
            if animal.type == type:
                ret = animal
                break 
            else:
                self.stack.append(animal)

        while len(self.stack) > 0:
            self.queue.appendleft(self.stack.pop())

        return ret 

    def dequeueCat(self):
        return self._dequeueType("Cat")

    def dequeueDog(self):
        return self._dequeueType("Dog")
        


    
animalShelter = AnimalShelter()
print(animalShelter)
animalShelter.enqueue('1', type = "Dog")
animalShelter.enqueue('2', type = "Dog")
animalShelter.enqueue('3', type = "Cat")
a = animalShelter.dequeueDog()
if type(a) == Animal:
    print(a.name)
else:
    print(a)

