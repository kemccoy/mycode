#!/usr/bin/env python3
# I want a red 2020 Lambo
# I want a gold 1969 Camaro
# I want a black 2009 Silverado
cars = [{'type': 'Lambo', 'year' : '2020', 'color': 'red'}, {'type': 'Camaro', 'year' : '1969', 'color': 'gold'}, {'type': 'Silverado', 'year' : '2009', 'color': 'black'}]
#car1 = f"I want a {cars[0]['color']} {cars[0]['type']} from {cars[0]['year']}"
#car2 = f"I want a {cars[1]['color']} {cars[1]['type']} from {cars[1]['year']}"
#car3 = f"I want a {cars[2]['color']} {cars[2]['type']} from {cars[2]['year']}"


#print(car1)
#print(car2)
#print(car3)

# For loop example:
for car in cars:
    print(f"I want a {car['color']} {car['type']} from {car['year']}.")
