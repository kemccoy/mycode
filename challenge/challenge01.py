#!/usr/bin/env python3
pets = ['fido', 'spot', 'fluffy']
print(pets)
#new_pets = ['ginger', 'rex', 'ruff']
#print(new_pets)
#pets.append(new_pets)
#print(pets)
pet1 = input("pet 1 name: ")
pet2 = input("pet 2 name: ")
pet3 = input("pet 3 name: ")
pets.append(pet1)
pets.insert(1, pet2)
pets = pets + [pet3]
print(pets)
print(enumerate(pets))
for ind, val in enumerate(pets):
    print(ind, val)
