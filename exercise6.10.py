small_list = [] #The idea is to have small_list store name + marks of someone
big_list = [] #and then store it to big_list. Then pop small_list empty and repeat
small_list.append((input("Write the name of the person: ")))
while small_list[0] != '':
    small_list.append(int((input("Write the mark: "))))
    while small_list[-1] <= 10 and small_list[-1] >= 0:
        small_list.append(int((input("Write more marks: "))))
    small_list.pop() #get rid of the last >10 or < 0
    big_list.append(list(small_list))
    small_list.clear()
    small_list.append((input("Write the name of the person: ")))
print("Mark of sudents:")
for i in big_list:
    print("Name: " + str(i[0]))
    for j in i:
        if j != i[0]: #just skip the first, more simple
            print(" "+str(j)+" -", end= "")
    print("")