print(" ------------------------------------------------")
print("|                                                |")
print("|    06whileLoop                                 |")
print("|    Name : Natalie                              |")
print("|    Version : 01                                |")
print("|                                                |")
print(" ------------------------------------------------")

x = str("IST")
answer = str(input("What is the name of this subject "))
if x == answer:
    print(" ")
    print (" Congratulations!!")
    print(" ")

while x != answer:
    print("Not Correct - try again")
    answer = str(input("What is the name of this subject "))
    if x == answer:
        print(" ")
        print (" Congratulations!!")
        print(" ")


