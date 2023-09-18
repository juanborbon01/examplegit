"""
fecha:18/09/2023
autor: juanrojas
objetivo: ejemplo de versionamiento con git de python
"""
import random

random_number = random.randint(1,10)
print(random_number)

for i in range(0,10):
    random_number = random.randrange(20,100,5)
    print(random_number)

print("----------------------")

for i in range(0,10):
    random_number = random.random()
    print(random_number)


print("----------------------")

for i in range(0,10):
    random_number = random.uniform(10.5,20.6)
    print(random_number)