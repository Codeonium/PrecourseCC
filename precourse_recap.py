name = input("What is your name? ")

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

if int(number) == 1:
    print("Wrong ..")
elif int(number) == 2:
    print("Wrong ..")
elif int(number) == 3:
    print("Wrong ..")
elif int(number) == 4:
    print("Wrong ..")
elif int(number) == 5:
    print("Wrong ..")
elif int(number) == 6:
    print("Wrong ..")
else:
    print(" Finally you got it right, your number: " + number + " it is the right number. Hey don't blame me... never trust a computer to play fair... Muaaahhhh" )