limit = int((input ("Write the limit: ")))
list_nums = []
adder = 0 #variable in which to store the sum of inputs
while adder < limit:
    list_nums.append(int((input("Write another number: "))))
    adder += list_nums[-1]
    if adder > limit:
        print("Sum of numbers is: "+str(adder)+" which is "+ str(adder-limit)+"too high, try again")
        adder -= list_nums[-1]
        list_nums.pop()
print("Limit is: "+ str(limit) + ". List of numbers summed:", end=" ")
for i in list_nums:
    print(str(i),end=" ")