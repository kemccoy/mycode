#!/usr/bin/env python3

message = 'Your official FortNight ranking is -----> '

# wrap connection in a float() to accept decimals as numbers
score = float(input("Please enter your best FortNight Score here ----> "))

# if input value was higher or equal to 25
if score >= 1000:
    message = message + 'FortNight Pro 3000! - Congratulations, you ROCK!!!'
elif score >= 500:
    message = message + 'FortNight Pro! - You\'re good, but not the best.... '
elif score >= 100:
    message = message + 'Getting There. You have some practice to do... '
else:
    message = message + 'Noob.. Try again... '
print(' ')
print(message)
print(' ')
