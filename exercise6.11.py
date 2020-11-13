import random
import time

min = int (input ( "Valor mínimo:"))
max = int (input ( "Valor máximo:"))
secreto = random.randint (min, max)
tries = 0
print("Adivina el número secreto *evil laugh*")
user_inp = int(input("Intentalo: "))
tries += 1
while user_inp != secreto:
    if user_inp > secreto:
        user_inp = int(input("Too high try again: "))
    else:
        user_inp = int(input("Too low try again: "))
    tries += 1
print("Nice, attempted: "+str(tries)+ " times.")