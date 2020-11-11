import random
import time

higher_vals = [] #Store all values that are higher than the number
lower_vals = [] #Store all values that are lower than the number
lower_vals.append(int (input ( "Valor mínimo:")))
higher_vals.append(int (input ( "Valor máximo:")))
attempt = int((higher_vals[0]-lower_vals[0])/2)
tries = 1
print("Think about a secret number, I'll guess it")
print("Is it "+ str(attempt)+"?")
user_inp = input()
while user_inp != "same":
    if user_inp == "higher":
        print("in high")
        lower_vals.append(attempt)
        attempt = attempt + int((higher_vals[-1]-lower_vals[-1])/2)
    else:
        print("in low")
        higher_vals.append(attempt)
        attempt = attempt - int((higher_vals[-1]-lower_vals[-1])/2)
    print("Is it "+ str(attempt)+"?")
    user_inp = input()
    tries +=1
print("Nice, attempted: "+str(tries)+ " times.")