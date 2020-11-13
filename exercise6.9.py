small_list = [] #The idea is to have small_list store name + phone of someone
big_list = [] #and then store it to big_list. Then pop small_list empty and repeat
small_list.append((input("Write the name of the person: ")))
while small_list[0] != 'S':
    small_list.append(int((input("Write the phone number of the person: "))))
    big_list.append(list(small_list))
    small_list.clear()
    small_list.append((input("Write the name of the person: ")))
for i in big_list:
    print("Name: " + str(i[0]) + ". Phone number: "+ str(i[1]))