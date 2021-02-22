name = input("What is your name? ").capitalize()

if len(name) < 1:
    print ("Am i not worthy of a name") 
elif len(name) == 1:
    print("Can't you give me a proper name?")
elif len(name) == 2:
    print("I know two letters are better than one but still that's no commitment at all...")
elif len(name) == 3:
    print ("That's a short name " + name + ", but i'll take it")
else:
    print("Welcome to this game i suppose... Jarvis... i meant " + name)


print (" I'm thinking of a number, from 1 to 6...")

number = input (" Guess what i'm thinking? ")

while True:
    if int(number) == 1:
        number = input("Wrong .. Try again!! What Number Am I Thinking? ")
    elif int(number) == 2:
        number = input("Wrong .. Try again!! What Number Am I Thinking? ")
    elif int(number) == 3:
        number = input("Wrong .. Try again!! What Number Am I Thinking? ")
    elif int(number) == 4:
        number = input(""" 4 ?!?!? I would never do that...
        Wrong .. Try again!! What Number Am I Thinking? """)
    elif int(number) == 5:
        number = input("Wrong .. Try again!! What Number Am I Thinking? ")
    elif int(number) == 6:
        number = input("Wrong .. Try again!! What Number Am I Thinking? ")
    else:
        print(" Finally you got it right, "+ name +" your number: " + number + " it is the right number. Hey don't blame me... never trust a computer to play fair... Muaaahhhh" )
        break