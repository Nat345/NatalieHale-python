#code is a bit inaccurate but cannot find problem

# variables 
def helloWorld1():
    print("Hello World")

def goodbyeWorld2():
    print(" ")
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")

def goodbyePerson3():
    name = input("What is your name ? ")
    print("Goodbye " + name)

def goodTeacher4():
    name = input("Teacher's name (try Mr Horan) ")
    if name == "Mr Horan":
        print("You are lucky, he is a great teacher.")
    else:
        print(name + " is an ok teacher")

def forloop5():
    for x in range(1, 500):
        print(x)

def whileloop6():
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

#start of code

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


x=("x")

variableInput = input("Enter an option ")

if variableInput == x:
    print(" ")
    print("----Start of Output ---------------------------")
    print(" ")
    print(" ")
    print("----End of Output -----------------------------")
    print(" ")
    print(" ")
    print(" ")


while variableInput != x:
    variableInput = input("Enter an option ")
    print("----Start of Output ---------------------------")
    if variableInput == "1":
        helloWorld1()
    if variableInput == "2":
        goodbyeWorld2()
    if variableInput == "3":
        goodbyePerson3()
    if variableInput == "4":
        goodTeacher4()
    if variableInput == "5":
        forloop5()
    if variableInput == "6":
        whileloop6()
    print("----End of Output -----------------------------")

    if variableInput == x:
        print(" ")
        print(" ")
else:
        print("----Start of Output ---------------------------")
        print(" ")
        print("invalid option")
        print(" ")
        print("----End of Output -----------------------------")


input("Press Enter to continue")

#clear
