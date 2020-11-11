num = int(input("Input the number"))
is_prime = True
i = 0
while i < num:
    if num % (i+1) == 0:
        if i+1 != num and i > 1:
            is_prime = False
            break
    i += 1
if is_prime:
    print("The number "+str(num)+" is prime")
else:
    print("The number "+str(num)+" is not prime")

#Creo que el for es más adecuado ya que directamente va aumentando el valor de i sin requerir una definicion antes
#y una línea de codigo dentro del while para aumentarla