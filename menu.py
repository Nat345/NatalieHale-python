def helloWorld1():
    print("----Start of Output ---------------------------")
    print("Hello World")
    print("----End of Output -----------------------------")

def goodbyeWorld2():
    print("----Start of Output ---------------------------")
    print(" ")
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")

def goodbyePerson3():
    print("----Start of Output ---------------------------")
    name = input("What is your name ? ")
    print("Goodbye " + name)
    print("----End of Output -----------------------------")

def goodTeacher4():
    print("----Start of Output ---------------------------")
    name = input("Teacher's name (try Mr Horan) ")
    if name == "Mr Horan":
        print("You are lucky, he is a great teacher.")
    else:
        print(name + " is an ok teacher")
    print("----End of Output -----------------------------")

def forloop5():
    print("----Start of Output ---------------------------")
    for x in range(1, 500):
        print(x)
    print("----End of Output -----------------------------")

def whileloop6():
    print("----Start of Output ---------------------------")
    x = str("IST")
    answer = str(input("What is the name of this subject "))
    if x == answer:
        print(" ")
        print(" ")
        print (" Congratulations!!")
        print(" ")
        print(" ")
        print(" ")

    while x != answer:
        print("Not Correct - try again")
        answer = str(input("What is the name of this subject "))
        if x == answer:
            print(" ")
            print(" ")
            print (" Congratulations!!")
            print(" ")
            print(" ")
            print(" ")
    print("----End of Output -----------------------------")




x=("x")

while input != x:
    print(" ------------------------------------------------")
    print("|                                                |")
    print("|    07Menu                                      |")
    print("|    Name : Natalie                              |")
    print("|    Version : 01                                |")
    print("|                                                |")
    print(" ------------------------------------------------")
    print("1. Hello World")
    print("2. Goodbye World")
    print("3. Goodbye Person")
    print("4. Good Teacher")
    print("5. forLoop")
    print("6. whileLoop")
    print("7. string Loop")
    print("8. Convert to ascii")
    print("9. Encode a string")
    print("x. To Exit")
    input("Enter an option ")
    if input == 1:
        helloWorld1()
    if input == 2:
        goodbyeWorld2()
    if input == 3:
        goodbyePerson3()
    if input == 4:
        goodTeacher4()
    if input == 5:
        forloop5()
    if input == 6:
        whileloop6()
    else:
        print("----Start of Output ---------------------------")
        print(" ")
        print("invalid option")
        print(" ")
        print("----End of Output -----------------------------")

input("Press Enter to continue")


